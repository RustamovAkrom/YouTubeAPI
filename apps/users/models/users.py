from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import TimestampedModel


class User(TimestampedModel, AbstractUser):
    avatar = models.ImageField(upload_to="user/avatar/%Y/%m/%d", blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created_at"]
        db_table = "users"

    def __str__(self):
        return self.email


class Channel(TimestampedModel):
    owner = models.ForeignKey(User, models.CASCADE, related_name="channels")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    subscribers = models.ManyToManyField(
        "User",
        symmetrical=False,
        related_name="subscribed_channels",
        verbose_name="subscribed",
        blank=True,
    )

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")
        ordering = ["-created_at"]
        db_table = "channels"

    def __str__(self):
        return self.name

    def follow(self, user):
        if not self.subscribers.filter(id=user.id).exists():
            self.subscribers.add(user)

    def unfollow(self, user):
        if self.subscribers.filter(id=user.id).exists():
            self.subscribers.remove(user)
