from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        db_table = "gl_tags"

    def __str__(self):
        return self.name
