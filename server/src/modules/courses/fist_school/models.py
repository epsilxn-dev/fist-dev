from django.db import models

from src.modules.faculty.structure.models import Department
from src.modules.tags.models import Tags


class FistLessoner(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Преподаватель (КШ)"
        verbose_name_plural = "Преподаватели (КШ)"
        db_table = "pr_school_teacher"

    def __str__(self):
        return f"{self.id}. {self.first_name} {self.last_name}"


class Direction(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название направления")
    description = models.TextField(verbose_name="Описание")
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    is_deleted = models.BooleanField(default=False)
    lessoners = models.ManyToManyField(FistLessoner)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ["id"]
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        db_table = "co_direction"

    def __str__(self):
        return self.name
