from django.urls import path

from .views import (Registration, Authorization, Logout, NewTokenPair, ConfirmEmail, ForgotPassword,
                    ForgotPasswordConfirm, CheckTokenView)

urlpatterns = [
    path("register/", Registration.as_view()),
    path("authorize/", Authorization.as_view()),
    path("logout/", Logout.as_view()),
    path("token_pair/", NewTokenPair.as_view()),
    path("confirm_email/", ConfirmEmail.as_view()),
    path("forgot_password/", ForgotPassword.as_view()),
    path("confirm_password/", ForgotPasswordConfirm.as_view()),
    path("check_token/", CheckTokenView.as_view())
]
