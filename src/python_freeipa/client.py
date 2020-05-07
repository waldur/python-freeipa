"""Lightweight FreeIPA JSON RPC client."""

import json
import logging
import socket

import requests

from python_freeipa.exceptions import (
    Denied,
    FreeIPAError,
    InvalidSessionPassword,
    KrbPrincipalExpired,
    PasswordExpired,
    PWChangeInvalidPassword,
    PWChangePolicyError,
    Unauthorized,
    UserLocked,
    parse_error,
)

try:
    import requests_gssapi
except ImportError as e:
    # Will raise if the user tries to login via Kerberos.
    requests_gssapi = e

try:
    import srvlookup
except ImportError as e:
    # Will raise if the user tires to do dns service discovery.
    srvlookup = e


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

    def __init__(self, host=None, verify_ssl=True, version=None, dns_discovery=True):
        """
        Initialize client with connection options.

        :param host: hostname to connect to, set None for dns service discovery
        :type host: str or None
        :param verify_ssl: verify SSL certificates for HTTPS requests
        :type verify_ssl: bool
        :param version: default client version, may be overwritten in individual requests
        :type version: str
        :param dns_discovery: if set to True, will try to use the current hosts domain name for dns discovery.
                           if set to a string, will use this string for dns discovery.
                           in both cases, it will try to strip as many parts left from a dot (.),
                           until it finds an idm server.
                           discovered IPA servers will by tried in order (priority, weight),
                           until one is found that will respond to our login request.
                           if host param is set, host param will always win, and no dns discovery is performed.
        :type dns_discovery: str
        """
        self._dns_discovery = dns_discovery
        self._host = host
        self._current_host = None
        self._base_url = 'https://{0}/ipa'.format(self._host)
        self._verify_ssl = verify_ssl
        self._version = version
        self._session = requests.Session()
        self._log = logging.getLogger(__name__)

    @property
    def current_host(self):
        return self._current_host

    @property
    def dns_discovered(self):
        if isinstance(self._dns_discovery, str):
            _domain = self._dns_discovery
        elif self._dns_discovery:
            _domain = socket.getfqdn()
        else:
            raise FreeIPAError('neither host specified, not dns_discovery enabled')
        while True:
            try:
                return srvlookup.lookup('ldap', 'tcp', _domain)
            except srvlookup.SRVQueryFailure:
                try:
                    _domain = _domain.split('.', 1)[1]
                except IndexError:
                    raise FreeIPAError('could not find any IPA Server using DNS lookup')

    @property
    def log(self):
        return self._log

    def _wrap_in_dns_discovery(self, function, *args, **kwargs):
        """
        Wrap a function in DNS discovery.

        :param function: the function to wrap
        :type function: callable
        :param args: the function's arguments
        :type args: list
        :param kwargs: the function's keyword arguments
        :type kwargs: dict
        """
        if self._host:
            self._current_host = self._host
            return function(*args, **kwargs)
        else:
            for host in self.dns_discovered:
                try:
                    self._current_host = host.hostname
                    return function(*args, **kwargs)
                except requests.exceptions.ConnectionError as err:
                    self.log.warning(
                        "Could not connect discovered host: {0}".format(err)
                    )
            raise FreeIPAError("Could not connect to any host")

    def login(self, username, password):
        """
        Login to FreeIPA server using username and password.

        :param username: user to connect
        :type username: str
        :param password: password of the user
        :type password: str
        :raises Unauthorized: raised if credentials are invalid.
        """
        return self._wrap_in_dns_discovery(self._login, username, password)

    def _login(self, username, password):
        """
        private function, use login instead
        """
        login_url = 'https://{0}/ipa/session/login_password'.format(self._current_host)
        headers = {
            'Referer': login_url,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain',
        }
        data = {'user': username, 'password': password}
        response = self._session.post(
            login_url, headers=headers, data=data, verify=self._verify_ssl
        )

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

        In order to use this method, the package ```requests_gssapi`` <https://pypi.org/project/requests-gssapi/>`_
        must be installed. There must already be a Kerberos Ticket-Granting Ticket (TGT) cached in a Kerberos credential
        cache. Whether a TGT is available can be easily determined by running the klist command. If no TGT is available,
        then it first must be obtained by running the kinit command, or pointing the ``$KRB5CCNAME`` environment
        variable to a credential cache with a valid TGT.

        :raises Unauthorized: raised if credentials are invalid.
        :raises ImportError: raised if the ``requests_gssapi`` module is unavailable.
        """
        return self._wrap_in_dns_discovery(self._login_kerberos)

    def _login_kerberos(self):
        """
        private function, use login_kerberos instead
        """
        if isinstance(requests_gssapi, ImportError):
            raise requests_gssapi

        login_url = 'https://{0}/ipa/session/login_kerberos'.format(self._current_host)
        headers = {'Referer': 'https://{0}/ipa'.format(self._current_host)}
        response = self._session.post(
            login_url,
            headers=headers,
            verify=self._verify_ssl,
            auth=requests_gssapi.HTTPSPNEGOAuth(),
        )

        if not response.ok:
            raise Unauthorized(response.text)

        self.log.info(
            'Successfully logged to {0} using Kerberos credentials.'.format(
                self._current_host
            )
        )

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
        :type method: str
        :param args: optional positional argument or list of arguments
        :type args: list or string
        :param params: optional named parameters
        :type params: dict
        :return: parsed response from the request
        :rtype: dict
        :raises FreeIPAError: if the response code is not OK
        """
        session_url = 'https://{0}/ipa/session/json'.format(self.current_host)
        headers = {
            'Referer': 'https://{0}/ipa'.format(self.current_host),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        if not args:
            args = []
        elif not isinstance(args, list):
            args = [args]

        if not params:
            params = {}

        if self._version:
            params.setdefault('version', self._version)

        data = {'method': method, 'params': [args, params]}

        self.log.debug(
            'Making {method} request to {url} with arguments {args} and params {params}'.format(
                method=method, url=session_url, args=args, params=params
            )
        )

        response = self._session.post(
            session_url, headers=headers, data=json.dumps(data), verify=self._verify_ssl
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

    def change_password(self, username, new_password, old_password, otp=None):
        """
        Set the password of a user. (Does not expire)

        :param username: User login (username)
        :type username: str
        :param new_password: New password for the user
        :type new_password: str
        :param old_password: Users old password
        :type old_password: str
        :param otp: User's OTP token if they have one
        :type otp: str or None
        """
        return self._wrap_in_dns_discovery(
            self._change_password, username, new_password, old_password, otp
        )

    def _change_password(self, username, new_password, old_password, otp=None):
        """
        private function, use change_password instead
        """
        password_url = 'https://{0}/ipa/session/change_password'.format(
            self.current_host
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/plain',
        }

        data = {
            'user': username,
            'new_password': new_password,
            'old_password': old_password,
        }
        if otp:
            data['otp'] = otp

        response = self._session.post(
            password_url, headers=headers, data=data, verify=self._verify_ssl
        )

        if not response.ok:
            raise FreeIPAError(message=response.text, code=response.status_code)

        pwchange_result = response.headers.get('X-IPA-Pwchange-Result', None)
        if pwchange_result != 'ok':
            if pwchange_result == 'invalid-password':
                raise PWChangeInvalidPassword(
                    message=response.text, code=response.status_code
                )
            elif pwchange_result == 'policy-error':
                policy_error = response.headers.get('X-IPA-Pwchange-Policy-Error', None)
                raise PWChangePolicyError(
                    message=response.text,
                    code=response.status_code,
                    policy_error=policy_error,
                )
            else:
                raise FreeIPAError(message=response.text, code=response.status_code)
        return response
