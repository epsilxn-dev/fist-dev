from django.contrib.auth.models import AbstractUser
from django.db import models


def upload_to(instance, file):
    ext = file.split(".")[-1]
    return f"users/{instance.id}/avatar.{ext}"


class Person(AbstractUser):
    patronymic = models.CharField(max_length=32, verbose_name="Отчество", default=None, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    is_confirmed_email = models.BooleanField(default=False, verbose_name="Почта подтверждена?")
    token_email = models.TextField(verbose_name="Токен для подтверждения",
                                   null=True, blank=True, default=None)
    token_password_change = models.CharField(max_length=1024, verbose_name="Токен для замены пароля",
                                             null=True, blank=True, default=None)
    avatar = models.ImageField(upload_to=upload_to, verbose_name="Аватар", blank=True, null=True, default="not-found.png")
    discord = models.CharField(max_length=32, verbose_name="Discord", blank=True, null=True, default=None)
    skype = models.CharField(max_length=64, verbose_name="Skype", blank=True, null=True, default=None)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True, default="Не указано")
    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "pr_person"

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
        return self.username
