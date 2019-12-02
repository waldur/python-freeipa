"""Exceptions module for FreeIPA client."""


class FreeIPAError(Exception):
    """Base exception class for FreeIPA client."""

    message = 'An unknown exception occurred.'

    def __init__(self, message=None, code=None):
        """Initialize exception class with optional message and code."""
        if message:
            self.message = message
        if code:
            self.code = code

    def __str__(self):
        """Serialize exception to string using it's message."""
        return str(self.message)


class PWChangeInvalidPassword(FreeIPAError):
    """Raised when the current password is not correct while trying to change
    passwords."""


class PWChangePolicyError(FreeIPAError):
    """Raised when changing a password but the new password doesn't fit the
    password policy."""

    # Carry along some extra information about the policy error.
    def __init__(self, message=None, code=None, policy_error=None):
        if policy_error:
            self.policy_error = policy_error
        super(PWChangePolicyError, self).__init__(message=message, code=code)


class BadRequest(FreeIPAError):
    """General purpose exception class."""


class Unauthorized(BadRequest):
    """Raised when invalid credentials are provided."""

    message = 'Unauthorized: bad credentials.'


class PasswordExpired(Unauthorized):
    """Raised when logging in with an expired password."""

    message = 'PasswordExpired: password expired.'


class KrbPrincipalExpired(Unauthorized):
    """Raised when Kerberos Principal is expired."""


class Denied(Unauthorized):
    """Raised on ACI authorization error."""


class InvalidSessionPassword(Unauthorized):
    """Raised when IPA cannot obtain a TGT for a principal."""


class UserLocked(Unauthorized):
    """Raised when a user account is locked."""

    message = 'UserLocked: user account is locked.'


class NotFound(BadRequest):
    """Raised when an entry is not found."""


class AlreadyActive(BadRequest):
    """Raised when an entry is made active that is already active."""


class AlreadyInactive(BadRequest):
    """Raised when an entry is made inactive that is already inactive."""


class ValidationError(BadRequest):
    """Raised when a parameter value fails a validation rule."""


class DuplicateEntry(BadRequest):
    """Raised when an entry already exists."""

    message = "Entry already exists"


class UnknownOption(BadRequest):
    """Raised when a command is called with unknown options."""


error_codes = {
    1201: InvalidSessionPassword,
    1202: PasswordExpired,
    1203: KrbPrincipalExpired,
    1204: UserLocked,
    2100: Denied,
    3005: UnknownOption,
    3009: ValidationError,
    4001: NotFound,
    4002: DuplicateEntry,
    4009: AlreadyActive,
    4010: AlreadyInactive,
}


def parse_error(error):
    """Convert error object to FreeIPA exception class."""
    message = error['message']
    code = error['code']
    exception_class = error_codes.get(code, BadRequest)
    raise exception_class(message, code)


def parse_group_management_error(data):
    """Convert group management error object to FreeIPA exception class."""
    failed = data['failed']
    if failed['member']['group'] or failed['member']['user']:
        raise ValidationError(failed)


def parse_hostgroup_management_error(data):
    """Convert host group management error object to FreeIPA exception class."""
    failed = data['failed']
    if failed['member']['host'] or failed['member']['hostgroup']:
        raise ValidationError(failed)
