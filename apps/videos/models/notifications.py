from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel
from apps.videos.choices import NotificationType


class Notification(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="notifications")
    sender = models.ForeignKey("users.User", models.SET_NULL, null=True, blank=True, related_name="sent_notifications")
    notification_type = models.CharField(max_length=50, choices=NotificationType.choices, verbose_name=_("Notification Type"))
    message = models.TextField(verbose_name=_("Message"))
    related_object_id = models.IntegerField(null=True, blank=True, verbose_name=_("Related Object ID"))
    is_read = models.BooleanField(default=False, verbose_name=_("Is Read"))

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ['-created_at']
        db_table = "notifications"

    @classmethod
    def unread_notifications(cls, user):
        return cls.objects.filter(user=user, is_read=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()
        
    def __str__(self):
        return f"{self.user} - {self.notification_type}"
    