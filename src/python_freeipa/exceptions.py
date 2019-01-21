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
        return self.message


class BadRequest(FreeIPAError):
    """General purpose exception class."""


class Unauthorized(BadRequest):
    """Raised when invalid credentials are provided."""

    message = 'Unauthorized: bad credentials.'


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
