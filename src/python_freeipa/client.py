import json
import logging
import requests

from .exceptions import *

logger = logging.getLogger(__name__)


class Client(object):
    """
    Lightweight FreeIPA JSON RPC client.
    """

    def __init__(self, host, verify_ssl=True, version=None):
        """
        :param host: hostname to connect to
        :type host: string
        :param verify_ssl: verify SSL certificates for HTTPS requests, defaults to True
        :type verify_ssl: bool
        :param version: default client version, may be overwritten in individual requests
        :type version: string
        """
        self._host = host
        self._base_url = 'https://{0}/ipa'.format(self._host)
        self._verify_ssl = verify_ssl
        self._version = version
        self._session = requests.Session()

    def login(self, username, password):
        """
        Login to FreeIPA server using username and password.
        
        :param username: user to connect
        :type username: string
        :param password: password of the user
        :type password: string
        :raises Unauthorized:
        """
        login_url = '{0}/session/login_password'.format(self._base_url)
        headers = {
            'Referer': login_url,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain'
        }
        data = {'user': username, 'password': password}
        response = self._session.post(login_url, headers=headers, data=data, verify=self._verify_ssl)

        if not response.ok:
            raise Unauthorized(response.content)

        logger.info('Successfully logged in as {0}'.format(username))

    def _request(self, method, args=None, params=None):
        """
        Make an HTTP request to FreeIPA JSON RPC server.

        :param method: RPC method name is required
        :type method: string
        :param args: optional positional argument or list of arguments
        :type args: list or string
        :param params: optional named parameters
        :type params: dict
        :return: parsed response from the request
        :rtype: dict
        :raises FreeIPAError: if the response code is not OK
        """
        session_url = '{0}/session/json'.format(self._base_url)
        headers = {
            'Referer': self._base_url,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if not isinstance(args, list):
            args = [args]

        if not params:
            params = {}

        if self._version:
            params.setdefault('version', self._version)

        data = {
            'method': method,
            'params': [args, params]
        }

        logger.debug('Making {method} request to {url} with arguments {args} and params {params}'.format(
            method=method, url=session_url, args=args, params=params))

        response = self._session.post(
            session_url,
            headers=headers,
            data=json.dumps(data),
            verify=self._verify_ssl
        )

        if response.status_code == 401:
            raise Unauthorized()

        if not response.ok:
            raise FreeIPAError(message=response.content, code=response.status_code)

        result = response.json()
        error = result['error']
        if error:
            parse_error(error)
        else:
            return result['result']

    def user_add(self, username, first_name, last_name, full_name, noprivate=False,
                 mail=None, ssh_key=None, job_title=None,
                 preferred_language=None, disabled=False, **kwargs):
        """
        Add a new user. Username corresponds to UID field of user.

        :param username: User login, it should be alphanumeric and maximum length is 255.
        :type username: string
        :param first_name: First name
        :type first_name: string
        :param last_name: Last name
        :type last_name: string
        :param full_name: Full name
        :type full_name: string
        :param noprivate: Don't create user private group
        :type noprivate: bool
        :param mail: Email address
        :type mail: string or list
        :param ssh_key: SSH public key
        :type ssh_key: string or list
        :param job_title: Job title
        :type job_title: string
        :param preferred_language: Preferred language ISO code
        :type preferred_language: string
        :param disabled: Account disabled
        :type disabled: bool
        """
        params = {
            'all': True,
            'givenname': first_name,
            'sn': last_name,
            'cn': full_name,
        }

        if noprivate:
            params['noprivate'] = noprivate

        if mail:
            params['mail'] = mail

        if ssh_key:
            params['ipasshpubkey'] = ssh_key

        if job_title:
            params['title'] = job_title

        if preferred_language:
            params['preferredlanguage'] = preferred_language

        if disabled:
            params['nsaccountlock'] = disabled

        params.update(kwargs)
        data = self._request('user_add', username, params)
        return data['result']

    def user_find(self, criteria=None, **kwargs):
        """
        Search for users.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        params = {
            'all': True,
            'no_members': False,  # Suppress processing of membership attributes.
            'sizelimit': 0,  # Maximum number of entries returned (0 is unlimited)
            'whoami': False  # Display user record for current Kerberos principal.
        }
        params.update(kwargs)
        return self._request('user_find', criteria, params)

    def user_show(self, username):
        """
        Display information about a user.

        :param username: User login.
        :type username: string
        """
        data = self._request('user_show', username, {'all': True, 'raw': False})
        return data['result']

    def user_status(self, username):
        """
        Get lockout status of a user account.

        :param username: User login.
        :type username: string
        """
        return self._request('user_status', username, {'all': True, 'raw': False})

    def user_disable(self, username):
        """
        Disable a user account.

        :param username: User login.
        :type username: string
        """
        self._request('user_disable', username)

    def user_enable(self, username):
        """
        Enable a user account.

        :param username: User login.
        :type username: string
        """
        self._request('user_enable', username)

    def user_mod(self, username, **kwargs):
        """
        Modify a user.

        :param username: User login.
        :type username: string
        """
        params = {
            'all': False,  # Retrieve and print all attributes from the server.
            'no_members': False,  # Suppress processing of membership attributes.
            'raw': False,  # Print entries as stored on the server.
            'rights': False,  # Display the access rights of this entry.
        }
        params.update(kwargs)
        data = self._request('user_mod', username, params)
        return data['result']

    def user_del(self, username, skip_errors=False, soft_delete=False):
        """
        Delete a user.

        :param username: User login.
        :type username: string
        :param skip_errors: Continuous mode: Don't stop on errors.
        :type skip_errors: bool
        :param soft_delete: Mark user as deleted instead of removing record.
        :type soft_delete: bool
        """
        params = {
            'continue': skip_errors,
            'preserve': soft_delete,
        }
        return self._request('user_del', username, params)

    def group_add(self, group, **kwargs):
        """
        Create a new group.

        :param group: Group name, it should be alphanumeric and maximum length is 255.
        """
        params = {'all': True}
        params.update(kwargs)
        data = self._request('group_add', group, params)
        return data['result']

    def group_del(self, group, skip_errors=False):
        """
        Delete a group.

        :param group: Group name
        :param skip_errors: Continuous mode: Don't stop on errors.
        :type skip_errors: bool
        """
        params = {'continue': skip_errors}
        self._request('group_del', group, params)

    def group_add_member(self, group, users=None, groups=None, skip_errors=False, **kwargs):
        """
        Add members to a group.

        :param group: Group name.
        :param users: Users to add.
        :type users: string or list
        :param groups: Groups to add.
        :type groups: string or list
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {
            'all': True,
            'raw': True,
            'user': users,
            'group': groups,
        }
        params.update(kwargs)
        data = self._request('group_add_member', group, params)
        if not skip_errors:
            parse_group_management_error(data)
        return data['result']

    def group_remove_member(self, group, users=None, groups=None, skip_errors=False, **kwargs):
        """
        Remove members from a group.

        :param group: Group name.
        :param users: Users to remove.
        :type users: string or list
        :param groups: Groups to remove.
        :type groups: string or list
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {
            'all': False,
            'no_members': False,
            'raw': False,
            'user': users,
            'group': groups,
        }
        params.update(kwargs)
        data = self._request('group_remove_member', group, params)
        if not skip_errors:
            parse_group_management_error(data)
        return data['result']

    def group_find(self, criteria=None, **kwargs):
        """
        Search for groups.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        params = {
            'all': True,
            'sizelimit': 0
        }
        params.update(kwargs)
        return self._request('group_find', criteria, params)

    def group_show(self, group, **kwargs):
        """
        Display information about a named group.

        :param group: Group name.
        """
        params = {
            'all': True,
            'raw': False
        }
        params.update(kwargs)
        data = self._request('group_show', group, params)
        return data['result']

    def group_mod(self, group, **kwargs):
        """
        Modify a group.

        :param group: Group name.
        """
        params = {
            'all': False,
            'no_members': False,
            'raw': False,
            'rights': False,
        }
        params.update(kwargs)
        data = self._request('group_mod', group, params)
        return data['result']
