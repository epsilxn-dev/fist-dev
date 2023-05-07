from rest_framework import routers
from .views import TagViewSet, TagSearcher
from django.urls import path

router = routers.DefaultRouter()
router.register("tags", TagViewSet)
urlpatterns = [
    path("tags/contents/", TagSearcher.as_view())
] + router.urls
