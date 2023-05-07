from django.contrib.auth import get_user_model
from django.db import models
from tinymce.models import HTMLField

from src.modules.tags.models import Tags

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name="Тайтл")
    description = models.TextField(verbose_name="Описание")
    text = HTMLField(verbose_name="Текст")
    created_at = models.DateField(auto_now_add=True, verbose_name="Создано")
    views = models.IntegerField(default=0, blank=True, verbose_name="Просмотров")
    tags = models.ManyToManyField(Tags, verbose_name="Теги")
    image = models.ImageField(upload_to="news", default="not-found.png")

    class Meta:
        ordering = ["id"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        db_table = "fc_news"

    def __str__(self):
        return f"{self.id}. {self.title}"


class NewsCommentary(models.Model):
    text = models.TextField(verbose_name="Комментарий")
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    parent_id = models.IntegerField(null=True, blank=True, verbose_name="Комментарий-родитель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        ordering = ["id"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        db_table = "fc_news_comments"

    def __str__(self):
        return f"News: {self.news_id}. {self.id} to {self.parent_id}"

