from django.contrib import admin

from .models import Idea, Commentary, Link


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "is_moderated")
    list_editable = ("is_moderated", )
    sortable_by = ("is_moderated", )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "idea")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "link")
