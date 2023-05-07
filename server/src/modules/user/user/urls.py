from django.urls import path
from rest_framework import routers
from .views import (UserViewSet, UserPasswordChange, UserAvatarChange, UserUsernameChange, UserPrivateDataChange,
                    UserEmailChange)

router = routers.DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("users/change/password/", UserPasswordChange.as_view()),
    path("users/change/avatar/", UserAvatarChange.as_view()),
    path("users/change/username/", UserUsernameChange.as_view()),
    path("users/change/private_data/", UserPrivateDataChange.as_view()),
    path("users/change/email/", UserEmailChange.as_view()),
] + router.urls
