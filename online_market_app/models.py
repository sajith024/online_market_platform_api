from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import OnlineMarketUserManager


class Role(models.Model):
    name = models.CharField(unique=True)

    def __str__(self) -> str:
        return self.name


class OnlineMarketUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    objects = OnlineMarketUserManager()


class OnlineMarketLogs(models.Model):
    log_date = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField()
    request_path = models.CharField()
    request_status = models.SmallIntegerField()
    response = models.JSONField()

    def __str__(self) -> str:
        return self.log_date