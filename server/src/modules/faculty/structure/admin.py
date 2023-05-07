from django.contrib import admin

from .models import Department, Specialty, Discipline, Lessoner, Graduate, Techs, Results


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "department")


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Lessoner)
class LessonerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "department")


@admin.register(Techs)
class TechAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Graduate)
class GraduateAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "specialty")
    ordering = ["id"]


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    ordering = ["id"]

