from django.db import models

from src.modules.tags.models import Tags


class Question(models.Model):
    """
    @TODO добавить отправку на почту, когда будет опубликовано
    """
    author_email = models.EmailField(null=True, blank=True, verbose_name="Почта автора")
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")
    is_ready_to_publish = models.BooleanField(default=False, verbose_name="Готово к публикации?")
    theme = models.CharField(max_length=32, verbose_name="Тема", blank=True, null=True, default=None)
    tags = models.ManyToManyField(Tags, verbose_name="Теги")

    class Meta:
        ordering = ["id"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        db_table = "fc_questions"

    def __str__(self):
        return self.question
