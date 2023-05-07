from django.contrib import admin
from .models import News, NewsCommentary


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "views", "created_at")
    sortable_by = ("views", )


@admin.register(NewsCommentary)
class NewsCommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "news")
