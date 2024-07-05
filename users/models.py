from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """ Модель пользователя """
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    avatar = models.ImageField(upload_to="user/", **NULLABLE, verbose_name="фото")
    token = models.CharField(max_length=100, **NULLABLE, verbose_name="token")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"