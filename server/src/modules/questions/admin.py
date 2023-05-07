from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "author_email", "is_ready_to_publish")
    sortable_by = ("is_ready_to_publish", )
    list_editable = ("is_ready_to_publish", )

