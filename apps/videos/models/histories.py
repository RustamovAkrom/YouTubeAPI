from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class WatchHistory(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="watch_histories")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="watch_histories")

    class Meta:
        verbose_name = _("Watch History")
        verbose_name_plural = _("Watch Histories")
        ordering = ['-created_at']
        db_table = "watch_histories"

    def __str__(self):
        return f"{self.user} (watched video): {self.video}"
