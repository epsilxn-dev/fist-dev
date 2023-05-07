from rest_framework.routers import DefaultRouter
from .views import NewsView, CommentaryView

router = DefaultRouter()
router.register("news", NewsView)
router.register("news-commentaries", CommentaryView)
urlpatterns = router.urls
