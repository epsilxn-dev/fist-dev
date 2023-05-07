from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import DepartmentView, SpecialtyView, DisciplineView, LessonerView, GraduateView


router = DefaultRouter()
router.register("departments", DepartmentView)
router.register("specialties", SpecialtyView)
router.register("disciplines", DisciplineView)
router.register("lessoners", LessonerView)
router.register("graduates", GraduateView)

urlpatterns = router.urls
