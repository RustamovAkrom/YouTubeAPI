from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel
from apps.videos.choices import NotificationType


class Notification(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="notifications")
    sender = models.ForeignKey("users.User", models.SET_NULL, null=True, blank=True, related_name="sent_notifications")
    notification_type = models.CharField(max_length=50, choices=NotificationType.choices)
    message = models.TextField()
    related_object_id = models.IntegerField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ['-created_at']
        db_table = "notifications"

    def mark_as_read(self):
        self.is_read = True
        self.save()
        
    def __str__(self):
        return f"{self.user} - {self.notification_type}"
    