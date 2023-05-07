from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import IdeaView, CommentaryView, LikeView, DislikeView

router = DefaultRouter()
router.register("ideas", IdeaView)
router.register("commentaries", CommentaryView)
urlpatterns = [
    path("ideas/likes/", LikeView.as_view()),
    path("ideas/dislikes/", DislikeView.as_view())
] + router.urls
