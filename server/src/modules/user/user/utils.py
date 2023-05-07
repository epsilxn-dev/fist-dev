from rest_framework.request import Request
from django.contrib.auth.hashers import check_password


def check_password_by_request(request: Request) -> bool:
    password = request.data.get("checkPassword")
    return password and check_password(password, request.user.password)
