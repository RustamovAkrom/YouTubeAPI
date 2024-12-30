from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class Notification(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ['-created_at']
        db_table = "notifications"

    def __str__(self):
        return f"{self.user} - {self.message}"
    