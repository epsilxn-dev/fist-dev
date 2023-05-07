import json
from collections import OrderedDict

from rest_framework.request import Request


class DataMiddleware(object):
    path_list = ["admin", "media", "static"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request, *args, **kwargs):
        response = self.get_response(request)
        root_path = request.path.split("/")[1]
        if root_path in self.path_list:
            return response
        try:
            response.data = OrderedDict({"data": dict(response.data)})
            response.content = json.dumps(response.data)
        except Exception as e:
            response.data = OrderedDict({"data": json.loads(json.dumps(response.data))})
            response.content = json.dumps(response.data)
        finally:
            return response
