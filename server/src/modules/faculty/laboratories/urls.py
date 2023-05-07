from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("laboratories", LaboratoryView)
router.register("projects", ProjectView)
urlpatterns = [
    path("projects/likes/", LikeView.as_view()),
    path("projects/dislikes/", DislikeView.as_view())
] + router.urls
