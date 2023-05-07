from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.core.exception import ClientException, ServerException
from src.core.security.jwt import generate_jwt_pair, decode_jwt
from src.core.utils.esia import get_refresh_dict

from .auth import AuthenticationSystem
from .models import User, AccessTokens, RefreshTokens
from .serializers import AuthorizationSerializer, RegistrationSerializer, AuthRespSerializer, \
    ConfirmRegistrationSerializer, ConfirmPasswordChangeSerializer, PasswordChangeSerializer

TAG = "RIA"  # registration identification authentication


class Registration(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer
    authentication_classes = []
    swagger_tags = [TAG]

    def post(self, request: Request, *args, **kwargs):
        data = self.serializer_class(data=request.data)
        if not data.is_valid():
            raise ClientException(data.errors)
        data.save()
        return Response(status=status.HTTP_201_CREATED)


class ConfirmEmail(CreateAPIView):
    swagger_tags = [TAG]
    permission_classes = [permissions.AllowAny]
    serializer_class = ConfirmRegistrationSerializer
    authentication_classes = []

    def post(self, request: Request, *args, **kwargs):
        token = request.data.get("token")
        candidates = User.objects.filter(token_email=token)
        if len(candidates) == 1:
            user = candidates[0]
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if not serializer.is_valid():
                raise ServerException()
            serializer.save()
            return Response(status=204)
        raise ClientException("Ошибка подтверждения почты", status.HTTP_400_BAD_REQUEST)


class Authorization(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorizationSerializer
    authentication_classes = []
    swagger_tags = [TAG]

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            candidate = User.objects.get(username=data.get("username"))
        except Exception as e:
            raise ClientException("Неверный логин или пароль", status.HTTP_400_BAD_REQUEST)
        if not candidate.is_confirmed_email:
            raise ClientException("Не подтверждена почта", status.HTTP_400_BAD_REQUEST)
        if check_password(data.get("password"), candidate.password):
            pair = generate_jwt_pair(candidate)
            response_data = {
                "access": pair.access.token,
                "user": candidate
            }
            response_cookie = get_refresh_dict(pair.refresh.token)
            response = Response(AuthRespSerializer(response_data).data, status=status.HTTP_200_OK)
            response.set_cookie(**response_cookie)
            return response
        raise ClientException("Неверный логин или пароль", status.HTTP_400_BAD_REQUEST)


class Logout(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [AuthenticationSystem]
    swagger_tags = [TAG]

    def delete(self, request: Request, *args, **kwargs):
        AccessTokens.objects.get(token=request.auth.token).delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.set_cookie(**get_refresh_dict())
        return response


class LogoutAll(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [AuthenticationSystem]
    swagger_tags = [TAG]

    def delete(self, request, *args, **kwargs):
        AccessTokens.objects.filter(user_id=request.user.id).delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.set_cookie(**get_refresh_dict())
        return response


class NewTokenPair(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    swagger_tags = [TAG]

    def post(self, request: Request, *args, **kwargs):
        token = request.COOKIES.get("refresh")
        if token is None or token == '':
            raise ClientException("Необходимо перезайти", status.HTTP_400_BAD_REQUEST)
        decoded_token = decode_jwt(token)
        if not decoded_token.is_valid:
            raise ClientException("Необходимо перезайти", status.HTTP_401_UNAUTHORIZED)
        refresh_model = RefreshTokens.objects.get(token=decoded_token.token)
        new_pair = generate_jwt_pair(refresh_model.user)  # User.objects.get(id=decoded_token.payload.get("id"))
        AccessTokens.objects.get(token=refresh_model.access.token).delete()
        response = Response({"access": new_pair.access.token}, status=status.HTTP_200_OK)
        response.set_cookie(**get_refresh_dict(new_pair.refresh.token))
        return response


class CheckTokenView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    swagger_tags = [TAG]

    def post(self, request: Request, *args, **kwargs):
        token = request.COOKIES.get("refresh")
        try:
            RefreshTokens.objects.get(token=token)
        except:
            return Response("0")
        return Response("1")


class ForgotPassword(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    swagger_tags = [TAG]
    serializer_class = PasswordChangeSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ClientException(serializer.errors)
        candidates = User.objects.filter(email=serializer.validated_data.get("email"))
        if len(candidates) == 1:
            serializer.instance = candidates[0]
            serializer.save()
            return Response(status=200)
        raise ServerException()


class ForgotPasswordConfirm(CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    swagger_tags = [TAG]
    serializer_class = ConfirmPasswordChangeSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ClientException(serializer.errors)
        candidates = User.objects.filter(token_password_change=serializer.validated_data.get("token"))
        if len(candidates) == 1:
            serializer.instance = candidates[0]
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        raise ServerException()
