from rest_framework import routers
from .views import LessonerViewSet, DirectionViewSet

router = routers.DefaultRouter()
router.register("fist_lessoners", LessonerViewSet)
router.register("fist_directions", DirectionViewSet)
urlpatterns = router.urls
