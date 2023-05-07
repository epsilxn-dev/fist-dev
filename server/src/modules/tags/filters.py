from django_filters import rest_framework as filters
from .models import Tags


class TagFilter(filters.FilterSet):
    class Meta:
        model = Tags
        fields = "__all__"
