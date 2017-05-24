class FreeIPAError(Exception):
    message = 'An unknown exception occurred.'

    def __init__(self, message=None, code=None):
        if message:
            self.message = message
        if code:
            self.code = code

    def __str__(self):
        return self.message


class BadRequest(FreeIPAError):
    """
    General purpose exception class.
    """


class Unauthorized(BadRequest):
    message = 'Unauthorized: bad credentials.'


class NotFound(BadRequest):
    """
    Raised when an entry is not found.
    """


class AlreadyActive(BadRequest):
    """
    Raised when an entry is made active that is already active.
    """


class AlreadyInactive(BadRequest):
    """
    Raised when an entry is made inactive that is already inactive.
    """


class ValidationError(BadRequest):
    """
    Raised when a parameter value fails a validation rule.
    """


class DuplicateEntry(BadRequest):
    """
    Raised when an entry already exists.
    """


class UnknownOption(BadRequest):
    """
    Raised when a command is called with unknown options.
    """


error_codes = {
    3005: UnknownOption,
    3009: ValidationError,
    4001: NotFound,
    4002: DuplicateEntry,
    4009: AlreadyActive,
    4010: AlreadyInactive,
}


def parse_error(error):
    message = error['message']
    code = error['code']
    exception_class = error_codes.get(code, BadRequest)
    raise exception_class(message, code)


def parse_group_management_error(data):
    failed = data['failed']
    if failed['member']['group'] or failed['member']['user']:
        raise ValidationError(failed)
