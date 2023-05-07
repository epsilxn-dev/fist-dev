from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

from src.modules.faculty.laboratories.models import Area
from src.modules.tags.models import Tags

User = get_user_model()


class Idea(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название идеи")
    description = models.TextField(verbose_name="Краткое описание")
    information = HTMLField(verbose_name="Описание задумки")
    is_moderated = models.BooleanField(default=False, verbose_name="Промодерировано?")
    image = models.ImageField(upload_to="ideas/", verbose_name="Изображение", default="not-found.png")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", verbose_name="Автор")
    tags = models.ManyToManyField(Tags, verbose_name="Теги")
    area_tech = models.ManyToManyField(Area)
    team = models.ManyToManyField(User, blank=True)
    likes = models.ManyToManyField(User, related_name="likes", verbose_name="Лайки", blank=True)
    dislikes = models.ManyToManyField(User, verbose_name="Дизлайки", blank=True, related_name="dislikes")

    class Meta:
        ordering = ["id"]
        verbose_name = "Идея"
        verbose_name_plural = "Идеи"
        db_table = "fc_ideas"

    def __str__(self):
        return f"{self.id}. {self.name}"


class Link(models.Model):
    link = models.TextField(verbose_name="Ссылка")
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        db_table = "fc_idea_links"

    def __str__(self):
        return f"{self.id}. {self.link}"


class Commentary(models.Model):
    message = models.TextField(verbose_name="Комментарий")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, verbose_name="Идея", default="not-found.png")
    parent_id = models.IntegerField(default=None, null=True, blank=True, verbose_name="Ответ на комментарий №")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Создано")

    class Meta:
        ordering = ["id"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        db_table = "fc_idea_comments"

    def __str__(self):
        return f"{self.id}"
