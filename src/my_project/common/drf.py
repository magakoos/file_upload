from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework_friendly_errors import settings
from rest_framework_friendly_errors.utils import is_pretty


# Формат ошибки:
# {
#   "code": "string",
#   "error_message": "string",
#   "field_errors": [
#     {
#       "field": "string",
#       "message": "string"
#     }
#   ]
# }


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response and settings.CATCH_ALL_EXCEPTIONS:
        exc = APIException(exc)
        response = exception_handler(exc, context)

    if response is not None:
        if is_pretty(response):
            return response
        error_message = response.data.get(
            'detail', str(exc.__class__.__name__)
        )
        error_code = settings.FRIENDLY_EXCEPTION_DICT.get(
            exc.__class__.__name__
        )
        if error_code is None:
            error_code = exc.error_code
        data = response.data
        errors = []
        for field, value in data.items():
            message = value[0] if isinstance(value, list) else value
            errors.append({"field": field, "message": message})

        response.data = {
            'code': error_code,
            'error_message': error_message,
            'field_errors': errors,
        }

    return response
