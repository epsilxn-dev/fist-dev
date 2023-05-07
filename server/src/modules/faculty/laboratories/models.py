from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField

from src.modules.faculty.structure.models import Specialty
from src.modules.tags.models import Tags

User = get_user_model()


class Area(models.Model):
    title = models.CharField(max_length=64, verbose_name="Название области", unique=True)

    class Meta:
        verbose_name = "Область технологий"
        verbose_name_plural = "Области технологий"
        db_table = "fc_area_tech"

    def __str__(self):
        return f"{self.title}"


class Laboratory(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")
    areas = models.ManyToManyField(Area, blank=True, verbose_name="Области технологий")
    description = models.CharField(max_length=1024, verbose_name="Описание", default="Нет описания")
    image = models.ImageField(upload_to="laboratories", default="not-found.png")
    text = models.TextField(verbose_name="Информация", default="")

    class Meta:
        ordering = ["id"]
        verbose_name = "Лаборатория"
        verbose_name_plural = "Лаборатории"
        db_table = "fc_laboratories"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    information = HTMLField(verbose_name="Текст")
    is_deleted = models.BooleanField(default=False, verbose_name="Удален?")
    is_moderated = models.BooleanField(default=False, verbose_name="Промодерирован?")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")
    teamlead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="teamlead", verbose_name="Главный разработчик")
    lab = models.ForeignKey(Laboratory, on_delete=models.CASCADE, null=True, verbose_name="Лаборатория")
    areas = models.ManyToManyField(Area, blank=True, verbose_name="Области технологий")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, verbose_name="Направление")
    contributors = models.ManyToManyField(User, verbose_name="Контрибьюторы")
    # ссылка на репозитории, etc...
    source = models.TextField(verbose_name="Ссылка на источник", blank=True, null=True, default=None)
    image = models.ImageField(upload_to="projects", default="not-found.png")
    likes = models.ManyToManyField(User, blank=True, related_name="project_likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="project_dislikes")

    class Meta:
        ordering = ["id"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        db_table = "fc_projects"

    def __str__(self):
        return self.name
