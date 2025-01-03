from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.shared.models import TimestampedModel
from apps.videos.choices import VideoReportTypeChoice


class VideoReport(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="reports")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="reports")
    report_type = models.CharField(
        max_length=50, 
        choices=VideoReportTypeChoice.choices, 
        default=VideoReportTypeChoice.OTHER
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Complaint from {self.user.username} about the video {self.video.title}"
    
    class Meta:
        verbose_name = _("Video Report")
        verbose_name_plural = ("Video Reports")
        ordering = ['-created_at']
        db_table = "video_reports"
