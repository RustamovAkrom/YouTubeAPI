from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class Channel(TimestampedModel):
    owner = models.ForeignKey("users.User", models.CASCADE, related_name="author_channels")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")
        ordering = ["-created_at"]
        db_table = "user_channels"

    def __str__(self):
        return self.name
