from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
from django.urls import reverse

__all__ = ("User",)


class User(AbstractUser):

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_absolute_url(self):
        return reverse("users:user", args=[self.pk])

    def clean(self):
        super().clean()

        model = self._meta.model
        if (
            model.objects.exclude(pk=self.pk)
            .filter(username__iexact=self.username)
            .exists()
        ):
            raise ValidationError(("A user with this username already exists."))
