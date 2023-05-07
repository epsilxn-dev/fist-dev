from django.db import models
from tinymce.models import HTMLField

from src.modules.tags.models import Tags


class Department(models.Model):
    """
    Модель кафедр
    """
    name = models.CharField(max_length=64, verbose_name="Название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    information = HTMLField(verbose_name="Текст")

    class Meta:
        ordering = ["id"]
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
        db_table = "fc_departments"

    def __str__(self):
        return self.name


class Techs(models.Model):
    name = models.CharField(max_length=64, verbose_name="Технология", unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
        db_table = "fc_tech_skills"

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=128, verbose_name="Короткое название")
    full_name = models.CharField(max_length=128, verbose_name="Полное название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    information = HTMLField(verbose_name="Текст")
    budget_seats = models.IntegerField(verbose_name="Бюджетных мест", null=True, blank=True, default=0)
    avatar = models.ImageField(upload_to="specialty_image", verbose_name="Изображение направления", default="not-found.png")
    stack_techs = models.ManyToManyField(Techs)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Кафедра")
    tags = models.ManyToManyField(Tags, verbose_name="Теги")
    price = models.IntegerField(default=0, verbose_name="Цена за год")
    years = models.CharField(max_length=10, verbose_name="Лет обучения", default="4")

    class Meta:
        ordering = ["id"]
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        db_table = "fc_specialties"

    def __str__(self):
        return self.name


class Results(models.Model):
    title = models.CharField(max_length=40, verbose_name="Строка с подитогом")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Направление")

    class Meta:
        ordering = ["id"]
        verbose_name = "В итоге"
        verbose_name_plural = "В итоге"
        db_table = "fc_specialty_results"

    def __str__(self):
        return self.title[:15]


class Discipline(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    information = HTMLField(verbose_name="Текст")
    specialties = models.ManyToManyField(Specialty, verbose_name="Направление")
    tags = models.ManyToManyField(Tags, verbose_name="Теги")

    class Meta:
        ordering = ["id"]
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        db_table = "fc_disciplines"

    def __str__(self):
        return self.name


def get_path_for_lessoner_image(instance, image) -> str:
    ext = image.split(".")[-1]
    return f"lessoners/{instance.id}/avatar.{ext}"


class Lessoner(models.Model):
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=32, verbose_name="Отчество", null=True)
    information = HTMLField(verbose_name="Текст")
    avatar = models.ImageField(upload_to=get_path_for_lessoner_image, default="not-found.png", verbose_name="Аватар")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name="Кафедра")
    disciplines = models.ManyToManyField(Discipline, blank=True, verbose_name="Дисциплины")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Теги")
    # Доцент, младший преподаватель...
    science_rank = models.CharField(max_length=90, verbose_name="Научная степень", default="")

    class Meta:
        ordering = ["id"]
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        db_table = "pr_fc_teachers"

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
        return f"{self.id}. {self.last_name} {self.first_name}"


def get_path_for_graduate_image(instance, image) -> str:
    ext = image.split(".")[-1]
    return f"graduates/{instance.id}/avatar.{ext}"


class Graduate(models.Model):
    fio = models.CharField(max_length=256, verbose_name="ФИО", default="Не указано")  # я не хотел так делать, меня заставили
    information = HTMLField(verbose_name="Текст")
    avatar = models.ImageField(upload_to=get_path_for_graduate_image, default="not-found.png", verbose_name="Аватар")
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Направление")
    rank = models.CharField(max_length=128, verbose_name="Текущая должность", blank=True, null=True, default=None)

    class Meta:
        ordering = ["id"]
        verbose_name = "Выпускник"
        verbose_name_plural = "Выпускники"
        db_table = "pr_fc_graduates"

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
        return f"{self.id}. {self.fio}"
