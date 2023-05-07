from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from tinymce.models import HTMLField

from src.modules.faculty.structure.models import Specialty
from src.modules.tags.models import Tags

User = get_user_model()


def non_empty_charfield_validation(value):
    if value == '':
        raise ValidationError(f"{value}s is empty")


def upload_image_to(instance, filename):
    ext = filename.split(".")[-1]
    return f"companies/{instance.id}/avatar.{ext}"


class Company(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    information = models.TextField(verbose_name="Информация")
    address = models.CharField(max_length=256, verbose_name="Адрес")
    avatar = models.ImageField(upload_to=upload_image_to, default="not-found.png", verbose_name="Аватар")

    class Meta:
        ordering = ["id"]
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        db_table = "wrk_companies"

    def save(self, *args, **kwargs):
        if self.pk is None:
            avatar = self.avatar
            self.avatar = None
            super().save(*args, **kwargs)
            self.avatar = avatar
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=128, verbose_name="Тайтл")
    description = models.CharField(max_length=1024, verbose_name="Описание", default="")
    salary_min = models.IntegerField(null=True, blank=True, verbose_name="Минимальная зп")
    salary_max = models.IntegerField(null=True, blank=True, verbose_name="Максимальная зп")
    currency_type = models.CharField(max_length=5, null=True, blank=True, verbose_name="Тип валюты")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.CharField(max_length=32, verbose_name="Почта")
    trash = models.IntegerField(verbose_name="Мусорность")
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    created_at = models.DateField(auto_now_add=True, verbose_name="Создано")
    work_exp = models.CharField(max_length=32, null=True, blank=True, verbose_name="Опыт работы",
                                default="Не требуется опыт работы")
    information = HTMLField(verbose_name="Информация")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")
    gender = models.CharField(max_length=15, verbose_name="Пол", default="Не указан")

    class Meta:
        ordering = ["id"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        db_table = "wrk_vacancies"

    def __str__(self):
        return f"{self.id}. {self.title}"


def upload_image_resume(instance, filename):
    ext = filename.split(".")[-1]
    return f"resumes/{instance.id}/avatar.{ext}"


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=32, verbose_name="Название навыка")

    class Meta:
        ordering = ["id"]
        verbose_name = "Скил"
        verbose_name_plural = "Скилы"

    def __str__(self):
        return self.name


class Resume(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=128, verbose_name="Тайтл", validators=[non_empty_charfield_validation])
    # Да, короткое описание == обычному описание, все вопросы к фронту
    description = models.CharField(max_length=1024, verbose_name="Описание",
                                   validators=[non_empty_charfield_validation])
    salary = models.CharField(max_length=50, default="Не указано", verbose_name="Желаемая зарплата")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.CharField(max_length=32, verbose_name="Почта", validators=[non_empty_charfield_validation])
    image = models.ImageField(upload_to=upload_image_resume, default="not-found.png", verbose_name="Аватар")
    work_exp = models.CharField(max_length=32, verbose_name="Опыт работы", default="Нет опыта работы")
    gender = models.CharField(max_length=10, verbose_name="Пол", default="Не указан")
    skills = models.ManyToManyField(Skill)
    specialization = models.ForeignKey(Specialty, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")

    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалено?")
    is_moderated = models.BooleanField(default=False, verbose_name="Промодерировано?")
    created_at = models.DateField(auto_now=True, verbose_name="Создано")
    updated_at = models.DateField(auto_now_add=True, verbose_name="Обновлено")

    class Meta:
        ordering = ["id"]
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        db_table = "wrk_resumes"

    def save(self, *args, **kwargs):
        if self.pk is None:
            avatar = self.avatar
            self.avatar = None
            super().save(*args, **kwargs)
            self.avatar = avatar
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        else:
            if self.title == '' or self.description == '' or self.email == '':
                raise ValidationError("Поле title, description или email пустое!")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}. {self.title}"
