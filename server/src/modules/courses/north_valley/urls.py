from django.urls import path
from .views import NorthValleyView

urlpatterns = [
    path("northvalley/", NorthValleyView.as_view())
]
