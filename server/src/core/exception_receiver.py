from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.conf import settings

from src.core.exception import ClientException, ServerException

def err_handler(err, cte):
    response = exception_handler(err, cte)
    if isinstance(err, ClientException) or isinstance(err, ServerException):
        if response is None:
            return Response({"errors": err.message}, status=err.resp_status)
        return response
    else:
        return response
