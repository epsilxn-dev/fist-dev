from django.contrib import admin
from .models import Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_editable = ("name", )
    ordering = ("id", )

