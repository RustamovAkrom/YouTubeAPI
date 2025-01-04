from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class Comment(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="comments")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="comments")
    message = models.TextField(verbose_name=_("Message"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-created_at']
        db_table = "video_comments"

    def __str__(self):
        return f"{self.user} - {self.video}"
