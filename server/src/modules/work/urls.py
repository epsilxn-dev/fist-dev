from rest_framework.routers import DefaultRouter
from .views import ResumeView, VacancyView, CompanyView

router = DefaultRouter()
router.register("resumes", ResumeView)
router.register("vacancies", VacancyView)
router.register("companies", CompanyView)
urlpatterns = router.urls
