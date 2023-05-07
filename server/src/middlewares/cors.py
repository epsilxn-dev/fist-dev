import datetime

from django.conf import settings


class CORSMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = settings.HOST_DOMAIN
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Headers"] = "Access-Control-Request-Method, Access-Control-Request-Headers, " \
                                                   "Accept-Encoding, Origin, X-Requested-With, Content-Type, Accept, " \
                                                   "Authorization, User-Agent, Sec-Fetch-Dest, Sec-Fetch-Mode, " \
                                                   "Sec-Fetch-Site, Connection, Referer"
        response["Access-Control-Request-Method"] = "GET, OPTIONS, POST, DELETE, PATCH, PUT"
        return response
