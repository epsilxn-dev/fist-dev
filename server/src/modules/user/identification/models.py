

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)

    class Meta:
        db_table = "pr_access_tokens"


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)

    class Meta:
        db_table = "pr_refresh_tokens"
