"""Lightweight FreeIPA JSON RPC client."""

import json
import logging

import requests

try:
    import requests_kerberos
except ImportError as e:
    # Will raise if the user tries to login via Kerberos.
    requests_kerberos = e

from .exceptions import (
    Denied, DuplicateEntry, FreeIPAError, InvalidSessionPassword,
    KrbPrincipalExpired, PWChangeInvalidPassword, PWChangePolicyError,
    PasswordExpired, Unauthorized, UserLocked, parse_error,
    parse_group_management_error, parse_hostgroup_management_error
)

logger = logging.getLogger(__name__)


class AuthenticatedSession(object):
    """
    Context manager class that automatically logs out upon exit.
    """
    def __init__(self, client, *login_arguments, **kwargs):
        """
        Constructs a new authenticated session with optional login arguments.

        When the ``__enter__`` method of is invoked, if the parameter ``logged_in`` is False, the class will attempt to
        login using the specified ``login_arguments`` (e.g. username and password) through ``Client.login``. If no
        login arguments is specified, it will attempt a Kerberos login via ``Client.login_kerberos``.

        :param client: an instance of a FreeIPA client
        :type client: ``Client``
        :param login_arguments: arguments to use to login upon enter, possibly empty.
        :param logged_in: True if the instance ``client`` is already logged in.
        :type logged_in: bool
        """
        self._client = client
        self._login_args = login_arguments
        self._logged_in = kwargs.get('logged_in', False)
        self._login_exception = None

    @property
    def logged_in(self):
        """
        Returns True if and only if the login attempt succeeded.
        """
        return self._logged_in

    @property
    def login_exception(self):
        """
        Returns the exception occurred during the login attempt, if any, otherwise None.
        """
        return self._login_exception

    def logout(self):
        """
        Logs out of the current session, if any is active.
        """
        if self.logged_in:
            self._client.logout()
            self._logged_in = False

    def __enter__(self):
        """
        Tries to perform a login, if necessary, using the login arguments specified at construction.

        This method does not throw, but will store any occurring exception in ``login_exception``.
        """
        if not self.logged_in:
            try:
                if len(self._login_args) > 0:
                    self._client.login(*self._login_args)
                else:
                    self._client.login_kerberos()
                self._logged_in = True
            except Exception as e:
                self._login_exception = e
                self._logged_in = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Logs out of the session, if necessary.
        """
        if self.logged_in:
            self.logout()


class Client(object):
    """Lightweight FreeIPA JSON RPC client."""

    def __init__(self, host, verify_ssl=True, version=None):
        """
        Initialize client with connection options.

        :param host: hostname to connect to
        :type host: string
        :param verify_ssl: verify SSL certificates for HTTPS requests
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
        :raises Unauthorized: raised if credentials are invalid.
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
            reason = response.headers.get('X-IPA-Rejection-Reason', None)
            if reason:
                if reason == 'password-expired':
                    raise PasswordExpired()
                elif reason == 'krbprincipal-expired':
                    raise KrbPrincipalExpired()
                elif reason == 'denied':
                    raise Denied()
                elif reason == 'invalid-password':
                    raise InvalidSessionPassword()
                elif reason == 'user-locked':
                    raise UserLocked()
            raise Unauthorized(response.text)

        logger.info('Successfully logged in as {0}'.format(username))

        return AuthenticatedSession(self, username, password, logged_in=True)

    def login_kerberos(self):
        """
        Login to FreeIPA server using existing Kerberos credentials.

        In order to use this method, the package ```requests_kerberos`` <https://pypi.org/project/requests-kerberos/>`_
        must be installed. There must already be a Kerberos Ticket-Granting Ticket (TGT) cached in a Kerberos credential
        cache. Whether a TGT is available can be easily determined by running the klist command. If no TGT is available,
        then it first must be obtained by running the kinit command, or pointing the ``$KRB5CCNAME`` environment
        variable to a credential cache with a valid TGT.

        :raises Unauthorized: raised if credentials are invalid.
        :raises ImportError: raised if the ``requests_kerberos`` module is unavailable.
        """
        if isinstance(requests_kerberos, ImportError):
            raise requests_kerberos

        login_url = '{0}/session/login_kerberos'.format(self._base_url)
        headers = {
            'Referer': self._base_url
        }
        response = self._session.post(login_url, headers=headers, verify=self._verify_ssl,
                                      auth=requests_kerberos.HTTPKerberosAuth())

        if not response.ok:
            raise Unauthorized(response.text)

        logger.info('Successfully logged using Kerberos credentials.')

        return AuthenticatedSession(self, logged_in=True)

    def logout(self):
        """
        Logs out of the FreeIPA session.
        """
        self._request('session_logout')

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

        if not args:
            args = []
        elif not isinstance(args, list):
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
            raise FreeIPAError(message=response.text, code=response.status_code)

        result = response.json()
        error = result['error']
        if error:
            parse_error(error)
        else:
            return result['result']

    def change_password(self, username, new_password, old_password):
        """
        Set the password of a user. (Does not expire)

        :param username: User login (username)
        :type username: string
        :param new_password: New password for the user
        :type new_password: string
        :param old_password: Users old password
        :type old_password: string
        """

        password_url = '{0}/session/change_password'.format(self._base_url)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain'
        }

        data = {'user': username, 'new_password': new_password, 'old_password': old_password}
        response = self._session.post(password_url, headers=headers, data=data, verify=self._verify_ssl)

        if not response.ok:
            raise FreeIPAError(message=response.text, code=response.status_code)

        pwchange_result = response.headers.get('X-IPA-Pwchange-Result', None)
        if pwchange_result != 'ok':
            if pwchange_result == 'invalid-password':
                raise PWChangeInvalidPassword(message=response.text, code=response.status_code)
            elif pwchange_result == 'policy-error':
                policy_error = response.headers.get('X-IPA-Pwchange-Policy-Error', None)
                raise PWChangePolicyError(message=response.text, code=response.status_code, policy_error=policy_error)
            else:
                raise FreeIPAError(message=response.text, code=response.status_code)
        return response

    def user_add(self, username, first_name, last_name, full_name, display_name=None,
                 noprivate=False, mail=None, ssh_key=None, job_title=None, gid_number=None, uid_number=None,
                 preferred_language=None, disabled=False, random_pass=False, initials=None, home_directory=None,
                 gecos=None, login_shell=None, user_password=None, street_address=None, city=None, state=None,
                 postal_code=None, telephone_number=None, mobile_number=None, pager_number=None, fax_number=None,
                 organization_unit=None, manager=None, car_license=None, user_auth_type=None,
                 user_class=None, radius_proxy_config=None, radius_proxy_username=None, department_number=None,
                 employee_number=None, employee_type=None, **kwargs):
        """
        Add a new user. Username corresponds to UID field of user.

        :param username: User login, it should be alphanumeric and maximum length is 32.
        :type username: string
        :param first_name: First name
        :type first_name: string
        :param last_name: Last name
        :type last_name: string
        :param full_name: Full name
        :type full_name: string
        :param display_name: Display name
        :type display_name: string
        :param noprivate: Don't create user private group
        :type noprivate: bool
        :param mail: Email address
        :type mail: string or list
        :param ssh_key: SSH public key
        :type ssh_key: string or list
        :param job_title: Job title
        :type job_title: string
        :param gid_number: gidNumber
        :type gid_number: string
        :param uid_number: uidNumber
        :type uid_number: string
        :param preferred_language: Preferred language ISO code
        :type preferred_language: string
        :param disabled: Account disabled
        :type disabled: bool
        :param random_pass: Generate a random user password
        :type random_pass: bool
        :param initials: Represent initials of user
        :type initials: string
        :param home_directory: Home directory field of user
        :type home_directory: string
        :param gecos: GECOS field is a comma-delimited list used to record general information about the user.
        :type gecos: string
        :param login_shell: Login shell field of user
        :type login_shell: string
        :param user_password: Prompt to set the user password
        :type user_password: string
        :param street_address: Street address field of user
        :type street_address: string
        :param city: City field of user
        :type city: string
        :param state: State/Province field of user
        :type state: string
        :param postal_code: ZIP code field of user
        :type postal_code: string
        :param telephone_number: Telephone number field of user
        :type telephone_number: string or list
        :param mobile_number: Mobile number field of user
        :type mobile_number: string or list
        :param pager_number: Pager number field of user
        :type pager_number: string or list
        :param fax_number: Fax number field of user
        :type fax_number: string or list
        :param organization_unit: Organization unit of user
        :type organization_unit: string
        :param manager: Manager field of user
        :type manager: string
        :param car_license: Car license of user
        :type car_license: string or list
        :param user_auth_type: Types of supported user authentication. Possible values(password, radius, otp)
        :type user_auth_type: string or list
        :param user_class: Category of user
        :type user_class: string
        :param radius_proxy_config: RADIUS proxy configuration
        :type radius_proxy_config: string
        :param radius_proxy_username: RADIUS proxy username
        :type radius_proxy_username: string
        :param department_number: Department number of user
        :type department_number: string
        :param employee_number: Employee number of user
        :type employee_number: string
        :param employee_type: Employee type of user
        :type employee_type: string
        """
        params = {
            'all': True,
            'givenname': first_name,
            'sn': last_name,
            'cn': full_name,
        }

        if gid_number:
            params['gidnumber'] = gid_number

        if uid_number:
            params['uidnumber'] = uid_number

        if display_name:
            params['displayname'] = display_name

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

        if random_pass:
            params['random'] = True

        if initials:
            params['initials'] = initials

        if home_directory:
            params['homedirectory'] = home_directory

        if gecos:
            params['gecos'] = gecos

        if login_shell:
            params['loginshell'] = login_shell

        if user_password:
            params['userpassword'] = user_password

        if street_address:
            params['street'] = street_address

        if city:
            params['l'] = city

        if state:
            params['st'] = state

        if postal_code:
            params['postalcode'] = postal_code

        if telephone_number:
            params['telephonenumber'] = telephone_number

        if mobile_number:
            params['mobile'] = mobile_number

        if pager_number:
            params['pager'] = pager_number

        if fax_number:
            params['facsimiletelephonenumber'] = fax_number

        if organization_unit:
            params['ou'] = organization_unit

        if manager:
            params['manager'] = manager

        if car_license:
            params['carlicense'] = car_license

        if user_auth_type:
            params['ipauserauthtype'] = user_auth_type

        if user_class:
            params['userclass'] = user_class

        if radius_proxy_config:
            params['ipatokenradiusconfiglink'] = radius_proxy_config

        if radius_proxy_username:
            params['ipatokenradiususername'] = radius_proxy_username

        if department_number:
            params['departmentnumber'] = department_number

        if employee_number:
            params['employeenumber'] = employee_number

        if employee_type:
            params['employeetype'] = employee_type

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

    def user_mod(self, username, first_name=None, last_name=None, full_name=None, display_name=None,
                 noprivate=False, mail=None, ssh_key=None, job_title=None,
                 preferred_language=None, disabled=False, random_pass=False, initials=None, home_directory=None,
                 gecos=None, login_shell=None, user_password=None, street_address=None, city=None, state=None,
                 postal_code=None, telephone_number=None, mobile_number=None, pager_number=None, fax_number=None,
                 organization_unit=None, manager=None, car_license=None, user_auth_type=None,
                 user_class=None, radius_proxy_config=None, radius_proxy_username=None, department_number=None,
                 employee_number=None, employee_type=None, **kwargs):
        """
        Modify a user.

        :param username: User login.
        :type username: string
        :param first_name: First name
        :type first_name: string
        :param last_name: Last name
        :type last_name: string
        :param full_name: Full name
        :type full_name: string
        :param display_name: Display name
        :type display_name: string
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
        :param random_pass: Generate a random user password
        :type random_pass: bool
        :param initials: Represent initials of user
        :type initials: string
        :param home_directory: Home directory field of user
        :type home_directory: string
        :param gecos: Gecos field of user
        :type gecos: string
        :param login_shell: Login shell field of user
        :type login_shell: string
        :param user_password: Prompt to set the user password
        :type user_password: string
        :param street_address: Street address field of user
        :type street_address: string
        :param city: City field of user
        :type city: string
        :param state: State/Province field of user
        :type state: string
        :param postal_code: ZIP code field of user
        :type postal_code: string
        :param telephone_number: Telephone number field of user
        :type telephone_number: string or list
        :param mobile_number: Mobile number field of user
        :type mobile_number: string or list
        :param pager_number: Pager number field of user
        :type pager_number: string or list
        :param fax_number: Fax number field of user
        :type fax_number: string or list
        :param organization_unit: Organization unit of user
        :type organization_unit: string
        :param manager: Manager field of user
        :type manager: string
        :param car_license: Car license of user
        :type car_license: string or list
        :param user_auth_type: Types of supported user authentication. Possible values(password, radius, otp)
        :type user_auth_type: string or list
        :param user_class: Category of user
        :type user_class: string
        :param radius_proxy_config: RADIUS proxy configuration
        :type radius_proxy_config: string
        :param radius_proxy_username: RADIUS proxy username
        :type radius_proxy_username: string
        :param department_number: Department number of user
        :type department_number: string
        :param employee_number: Employee number of user
        :type employee_number: string
        :param employee_type: Employee type of user
        :type employee_type: string
        """
        params = {
            'all': False,  # Retrieve and print all attributes from the server.
            'no_members': False,  # Suppress processing of membership attributes.
            'raw': False,  # Print entries as stored on the server.
            'rights': False,  # Display the access rights of this entry.
        }

        if first_name:
            params['givenname'] = first_name

        if last_name:
            params['sn'] = last_name

        if full_name:
            params['cn'] = full_name

        if display_name:
            params['displayname'] = display_name

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

        if random_pass:
            params['random'] = True

        if initials:
            params['initials'] = initials

        if home_directory:
            params['homedirectory'] = home_directory

        if gecos:
            params['gecos'] = gecos

        if login_shell:
            params['loginshell'] = login_shell

        if user_password:
            params['userpassword'] = user_password

        if street_address:
            params['street'] = street_address

        if city:
            params['l'] = city

        if state:
            params['st'] = state

        if postal_code:
            params['postalcode'] = postal_code

        if telephone_number:
            params['telephonenumber'] = telephone_number

        if mobile_number:
            params['mobile'] = mobile_number

        if pager_number:
            params['pager'] = pager_number

        if fax_number:
            params['facsimiletelephonenumber'] = fax_number

        if organization_unit:
            params['ou'] = organization_unit

        if manager:
            params['manager'] = manager

        if car_license:
            params['carlicense'] = car_license

        if user_auth_type:
            params['ipauserauthtype'] = user_auth_type

        if user_class:
            params['userclass'] = user_class

        if radius_proxy_config:
            params['ipatokenradiusconfiglink'] = radius_proxy_config

        if radius_proxy_username:
            params['ipatokenradiususername'] = radius_proxy_username

        if department_number:
            params['departmentnumber'] = department_number

        if employee_number:
            params['employeenumber'] = employee_number

        if employee_type:
            params['employeetype'] = employee_type
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

    def user_undel(self, username):
        """
        Undelete a user.

        :param username: User login.
        :type username: string
        """
        return self._request('user_undel', username)

    def passwd(self, login, password, current_password=None):
        """
        Set the password of a user.

        :param login: User login (username)
        :type login: string
        :param password: New password for the user
        :type password: string
        :param current_password: current password of the logged in user.
                                 Leave blank if resetting for another user,
                                 this will set the new password to expired
        :type current_password: string
        """
        if not current_password:  # resetting for another user
            params = {}
        else:  # resetting for current user
            params = {'current_password': current_password}

        data = self._request('passwd', args=[login, password], params=params)
        return data['result']

    def group_add(self, group, description=None, non_posix=False, external=False, no_members=False, **kwargs):
        """
        Create a new group.

        :param group: Group name, it should be alphanumeric and maximum length is 255.
        :type group: string
        :param description: Group description
        :type description: string
        :param non_posix: Create as non-POSIX group
        :type non_posix: bool
        :param external: Allow adding external non-IPA members from trusted domains
        :type external: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        """
        params = {'all': True}

        if description is not None:
            params['description'] = description

        if non_posix is not None:
            params['nonposix'] = non_posix

        if external is not None:
            params['external'] = external

        if no_members is not None:
            params['no_members'] = no_members

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

    def group_mod(self, group, description=None, posix=False, external=False, no_members=False, rename=None, **kwargs):
        """
        Modify a group.

        :param group: Group name.
        :type group: string
        :param description: Group description
        :type description: string
        :param posix: change to a POSIX group
        :type posix: bool
        :param external: Allow adding external non-IPA members from trusted domains
        :type external: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param rename: Rename the group object
        :type rename: string
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }
        if description:
            params['description'] = description

        if posix:
            params['posix'] = posix

        if external:
            params['external'] = external

        if no_members:
            params['no_members'] = no_members

        if rename:
            params['rename'] = rename

        params.update(kwargs)
        data = self._request('group_mod', group, params)
        return data['result']

    def automountkey_find(self, location, automount_map, key=None, criteria=None, **kwargs):
        """
        Search for the automount key.

        :param key: Automount key name.
        :type key: string
        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        :return:
        :rtype: dict
        """
        args = [
            location,
            automount_map
        ]

        if criteria:
            args.append(criteria)

        params = {
            'all': True,
            'raw': False,
        }

        if key:
            params['automountkey'] = key

        params.update(kwargs)

        data = self._request('automountkey_find', args, params)
        return data['result']

    def automountkey_add(self, key, mount_info, location, automount_map, **kwargs):
        """
        Create a new automount key.

        :param key: Automount key name
        :type key: string
        :param mount_info: Mount information
        :type mount_info: string
        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        :return: automount key data
        :rtype: dict
        """
        if self.automountkey_find(location, automount_map, key):
            raise DuplicateEntry()

        args = [
            location,
            automount_map
        ]

        params = {
            'all': True,
            'raw': False,
            'automountkey': key,
            'automountinformation': mount_info
        }
        params.update(kwargs)

        data = self._request('automountkey_add', args, params)
        return data

    def automountkey_mod(self, key, mount_info, automount_location, automount_map):
        """
        Modify an automount key.

        :param key: Automount key name
        :type key: string
        :param mount_info: Mount information
        :type mount_info: string
        :param automount_location: Automount location name
        :param: type string
        :param automount_map: Automount map name
        :type automount_map: string
        :return: automount key data
        :rtype: dict
        """
        args = [
            automount_location,
            automount_map
        ]

        params = {
            'all': True,
            'raw': False,
            'rights': False,
            'automountkey': key,
            'automountinformation': mount_info
        }

        data = self._request('automountkey_mod', args, params)
        return data

    def automountlocation_add(self, location, **kwargs):
        """
        Create a new automount location.

        :param location: Automount location name.
        :type location: string
        """
        params = {
            'all': True,
            'raw': False
        }
        params.update(kwargs)

        data = self._request('automountlocation_add', location, params)
        return data

    def automountlocation_del(self, location, skip_errors=False):
        """
        Delete an automount location.

        :param location: Automount location name.
        :type location: string
        """
        params = {'continue': skip_errors}
        data = self._request('automountlocation_del', location, params)
        return data

    def automountlocation_find(self, criteria=None, **kwargs):
        """
        Search for an automount location.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        params = {
            'all': True,
            'raw': False,
            'sizelimit': 0
        }
        params.update(kwargs)

        data = self._request('automountlocation_find', criteria, params)
        return data['result']

    def automountlocation_show(self, location, **kwargs):
        """
        Display an automount location.

        :param location: Automount location name.
        :type location: string
        """
        params = {
            'all': True,
            'raw': False,
            'rights': False
        }

        data = self._request('automountlocation_show', location, params)
        return data['result']

    def automountlocation_tofiles(self, location):
        """
        Generate automount files for a specific location.

        :param location: Automount location name
        :type location: string
        """
        data = self._request('automountlocation_tofiles', location)
        return data['result']

    def automountmap_add(self, location, automount_map, **kwargs):
        """
        Display an automount map.

        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        """
        args = [
            location,
            automount_map
        ]

        params = {
            'all': True,
            'raw': False
        }
        params.update(kwargs)

        data = self._request('automountmap_add', args, params)
        return data

    def automountmap_del(self, location, automount_map, skip_errors=False):
        """
        Delete an automount map.

        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        """
        args = [location, automount_map]
        params = {'continue': skip_errors}

        data = self._request('automountmap_del', args, params)
        return data

    def automountmap_find(self, location, criteria=None, **kwargs):
        """
        Find an automount map.

        :param location: Automount location name
        :type location: string
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        args = [location]
        if criteria:
            args.append(criteria)

        params = {
            'all': True,
            'raw': False,
            'sizelimit': 0
        }
        params.update(kwargs)

        data = self._request('automountmap_find', args, params)
        return data['result']

    def automountmap_mod(self, location, automount_map, description=None, **kwargs):
        """
        Modify an automount map.

        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        """
        args = [
            location,
            automount_map
        ]

        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }

        if description:
            params['description'] = description

        params.update(kwargs)

        data = self._request('automountmap_mod', args, params)
        return data

    def automountmap_show(self, location, automount_map, **kwargs):
        """
        Display an automount map.

        :param location: Automount location name
        :type location: string
        :param automount_map: Automount map name
        :type automount_map: string
        """
        args = [
            location,
            automount_map
        ]

        params = {
            'all': True,
            'raw': False,
            'rights': False
        }
        params.update(kwargs)

        data = self._request('automountmap_show', args, params)
        return data['result']

    def host_add(self, host, **kwargs):
        """
        Create a new host.

        :param host: Host name which should be alphanumeric and maximum length is 255
        :type host: string
        """
        params = {
            'all': True
        }
        params.update(kwargs)

        data = self._request('host_add', host, params)
        return data['result']

    def host_del(self, fqdn, skip_errors=False, updatedns=None):
        """
        Delete host from FreeIPA

        :param fqdn: Host name
        :type fqdn: string
        :param skip_errors: Continuous mode: Don't stop on errors
        :type skip_errors: bool
        :param updatedns: Remove A, AAAA, SSHFP and PTR records of the host(s) managed by IPA DNS
        :type updatedns: bool
        """
        params = {
            "continue": skip_errors
        }

        if updatedns:
            params['updatedns'] = updatedns

        data = self._request('host_del', fqdn, params)
        return data['result']

    def host_find(self, criteria=None, allattr=True, no_members=False, sizelimit=0, raw=False, **kwargs):
        """
        Search for hosts.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: int
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,             # Retrieve and print all attributes from the server. Affects command output
            'no_members': no_members,   # Suppress processing of membership attributes
            'sizelimit': sizelimit,     # Maximum number of entries returned (0 is unlimited)
            'raw': raw                  # Print entries as stored on the server. Only affects output format
        }
        params.update(kwargs)
        return self._request('host_find', criteria, params)

    def host_show(self, fqdn, rights=False, no_members=False, allattr=True, raw=False):
        """
        Display information about a host.

        :param fqdn: Host name
        :type fqdn: string
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        data = self._request('host_show', fqdn, {'all': allattr, 'rights': rights, 'no_members': no_members,
                                                 'raw': raw})
        return data['result']

    def hostgroup_add(self, hostgroup, description=None, no_members=False, **kwargs):
        """
        Create a new host group.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: string
        :param description: Host Group description
        :type description: string
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        """
        params = {'all': True}

        if description:
            params['description'] = description

        if no_members:
            params['no_members'] = no_members

        params.update(kwargs)
        data = self._request('hostgroup_add', hostgroup, params)
        return data['result']

    def hostgroup_del(self, hostgroup_name, skip_errors=False):
        """
        Delete a hostgroup

        :param hostgroup_name: Name of hostgroup
        :type hostgroup_name: string
        :param skip_errors: Continuous mode: Don't stop on errors
        :type skip_errors: bool
        """

        data = self._request('hostgroup_del', hostgroup_name, {'continue': skip_errors})
        return data['result']

    def hostgroup_find(self, criteria=None, allattr=True, no_members=False, sizelimit=0, raw=False, **kwargs):
        """
        Search for hostgroups

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param sizelimit: Maximum number of entries returned (0 is unlimited)
        :type sizelimit: int
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,             # Retrieve and print all attributes from the server. Affects command output
            'no_members': no_members,   # Suppress processing of membership attributes
            'sizelimit': sizelimit,     # Maximum number of entries returned (0 is unlimited)
            'raw': raw                  # Print entries as stored on the server. Only affects output format
        }
        params.update(kwargs)
        return self._request('hostgroup_find', criteria, params)

    def hostgroup_show(self, hostgroup, rights=False, no_members=False, allattr=True, raw=False):
        """
        Display information about a host.

        :param hostgroup: Hostgroup name
        :type hostgroup: string
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        data = self._request('hostgroup_show', hostgroup, {'all': allattr, 'rights': rights, 'no_members': no_members,
                             'raw': raw})
        return data['result']

    def hostgroup_mod(self, hostgroup, description=None, no_members=False, rights=False, allattr=False, raw=False,
                      **kwargs):
        """
        Modify a hostgroup.

        :param hostgroup: Group name.
        :type hostgroup: string
        :param description: Group description
        :type description: string
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param rights: Display the access rights of this entry (requires --all). See ipa man page for details
        :type rights: bool
        :param allattr: Retrieve and print all attributes from the server. Affects command output
        :type allattr: bool
        :param raw: Print entries as stored on the server. Only affects output format
        :type raw: bool
        """
        params = {
            'all': allattr,
            'raw': raw,
            'rights': rights,
            'no_members': no_members
        }
        if description:
            params['description'] = description

        params.update(kwargs)
        data = self._request('hostgroup_mod', hostgroup, params)
        return data['result']

    def hostgroup_add_members(self, hostgroup, no_members=False, host=None, hostgroups=None, skip_errors=False,
                              **kwargs):
        """
        Add members to a hostgroup.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: string
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param host: Hosts to add
        :type host: list or string
        :param hostgroups: Host group to add
        :type hostgroups: list or string
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {'all': True}

        if no_members:
            params['no_members'] = no_members

        if host:
            params['host'] = host

        if hostgroups:
            params['hostgroup'] = hostgroups

        params.update(kwargs)
        data = self._request('hostgroup_add_member', hostgroup, params)
        if not skip_errors:
            parse_hostgroup_management_error(data)
        return data['result']

    def hostgroup_remove_members(self, hostgroup, no_members=False, host=None, hostgroups=None, skip_errors=False,
                                 **kwargs):
        """
        Remove members from a hostgroup.

        :param hostgroup: Host Group name, it should be alphanumeric and maximum length is 255.
        :type hostgroup: string
        :param no_members: Suppress processing of membership attributes
        :type no_members: bool
        :param host: Hosts to remove
        :type host: list or string
        :param hostgroups: Host group to remove
        :type hostgroups: list or string
        :param skip_errors: Skip processing errors.
        :type skip_errors: bool
        """
        params = {'all': True}

        if no_members:
            params['no_members'] = no_members

        if host:
            params['host'] = host

        if hostgroups:
            params['hostgroup'] = hostgroups

        params.update(kwargs)
        data = self._request('hostgroup_remove_member', hostgroup, params)
        if not skip_errors:
            parse_hostgroup_management_error(data)
        return data['result']

    def dnsrecord_add(self, zone_name, record_name, **kwargs):
        """
        Create a new DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        :param record_name: DNS record name (e.g., host1)
        :type record_name: string
        """
        params = {'all': True}

        params.update(kwargs)
        data = self._request('dnsrecord_add', [zone_name, record_name], params)
        return data['result']

    def dnsrecord_del(self, zone_name, record_name, **kwargs):
        """
        Delete a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        :param record_name: DNS record name (e.g., host1)
        :type record_name: string
        """
        params = {}

        params.update(kwargs)
        self._request('dnsrecord_del', [zone_name, record_name], params)

    def dnsrecord_find(self, zone_name, criteria=None, **kwargs):
        """
        Search for DNS records.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        params = {
            'all': True,
            'sizelimit': 0
        }
        params.update(kwargs)
        return self._request('dnsrecord_find', [zone_name, criteria], params)

    def dnsrecord_show(self, zone_name, record_name, **kwargs):
        """
        Display information about a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        :param record_name: DNS record name (e.g., host1)
        :type record_name: string
        """
        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }
        params.update(kwargs)
        data = self._request('dnsrecord_show', [zone_name, record_name], params)
        return data['result']

    def dnsrecord_mod(self, zone_name, record_name, **kwargs):
        """
        Modify a DNS record.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        :param record_name: DNS record name (e.g., host1)
        :type record_name: string
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }

        params.update(kwargs)
        data = self._request('dnsrecord_mod', [zone_name, record_name], params)
        return data['result']

    def dnszone_add(self, zone_name, **kwargs):
        """
        Create a new DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        """
        params = {'all': True}

        params.update(kwargs)
        data = self._request('dnszone_add', zone_name, params)
        return data['result']

    def dnszone_del(self, zone_name, **kwargs):
        """
        Delete a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        """
        params = {}

        params.update(kwargs)
        self._request('dnszone_del', zone_name, params)

    def dnszone_find(self, criteria=None, **kwargs):
        """
        Search for DNS zones.

        :param criteria: A string searched in all relevant object attributes.
        :type criteria: string
        """
        params = {
            'all': True,
            'sizelimit': 0
        }
        params.update(kwargs)
        return self._request('dnszone_find', criteria, params)

    def dnszone_show(self, zone_name, **kwargs):
        """
        Display information about a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        """
        params = {
            'all': True,
            'raw': False,
            'rights': False,
        }
        params.update(kwargs)
        data = self._request('dnszone_show', zone_name, params)
        return data['result']

    def dnszone_mod(self, zone_name, **kwargs):
        """
        Modify a DNS zone.

        :param zone_name: DNS zone name (e.g., example.com)
        :type zone_name: string
        """
        params = {
            'all': False,
            'raw': False,
            'rights': False,
        }

        params.update(kwargs)
        data = self._request('dnszone_mod', zone_name, params)
        return data['result']
