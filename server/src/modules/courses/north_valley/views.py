from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.core.exception import ClientException
from src.core.utils.common import get_client_ip
from .serializers import NorthValleyRegistrationSerializer


class NorthValleyView(APIView):
    permission_classes = [AllowAny]
    swagger_tags = ["North Valley"]
    serializer_class = NorthValleyRegistrationSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ClientException(serializer.errors)
        user_agent = request.META.get("HTTP_USER_AGENT")
        ip = get_client_ip(request)
        serializer.save(user_agent=user_agent, ip=ip)
        return Response(status=201)

