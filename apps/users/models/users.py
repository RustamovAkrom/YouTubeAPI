from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import TimestampedModel


class User(TimestampedModel, AbstractUser):
    GENDER_CHOICES = [
        ("f", "Famale"),
        ("m", "Male"),
    ]
    avatar = models.ImageField(upload_to="user/avatar/%Y/%m/%d", blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_berthd = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]
        db_table = "users"
        
    def get_avatar(self):
        return self.avatar.url
    
    def __str__(self):
        return self.email

    