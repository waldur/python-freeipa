"""Lightweight FreeIPA JSON RPC client."""

import json
import logging

import requests

try:
    import requests_kerberos
except ImportError as e:
    # Will raise if the user tries to login via Kerberos.
    requests_kerberos = e

from python_freeipa.exceptions import Denied
from python_freeipa.exceptions import FreeIPAError
from python_freeipa.exceptions import InvalidSessionPassword
from python_freeipa.exceptions import KrbPrincipalExpired
from python_freeipa.exceptions import PWChangeInvalidPassword
from python_freeipa.exceptions import PWChangePolicyError
from python_freeipa.exceptions import PasswordExpired
from python_freeipa.exceptions import Unauthorized
from python_freeipa.exceptions import UserLocked
from python_freeipa.exceptions import parse_error


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
            except Exception as err:
                self._login_exception = err
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
        self._log = logging.getLogger(__name__)

    @property
    def log(self):
        return self._log

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

        self.log.info('Successfully logged in as {0}'.format(username))

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

        self.log.info('Successfully logged using Kerberos credentials.')

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

        self.log.debug('Making {method} request to {url} with arguments {args} and params {params}'.format(
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
