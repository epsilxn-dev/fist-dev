from django.contrib import admin
from .models import *


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "teamlead", "lab", "is_deleted", "is_moderated")
    list_editable = ("is_deleted", "is_moderated")
    sortable_by = ("is_deleted", "is_moderated")

