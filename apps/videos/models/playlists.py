from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class PlayList(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="playlists")
    channel = models.ForeignKey("videos.Channel", models.CASCADE, related_name="playlists")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _("Play List")
        verbose_name_plural = _("Play Lists")
        ordering = ['-created_at']
        db_table = "playlists"

    def __str__(self):
        return self.name


class PlayListVideo(TimestampedModel):
    playlist = models.ForeignKey("videos.PlayList", models.CASCADE, related_name="playlist_videos")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="playlist_videos")
    
    class Meta:
        verbose_name = _("Play List Video")
        verbose_name_plural = _("Play List Videos")
        ordering = ['-created_at']
        db_table = "playlist_videos"

    def __str__(self):
        return f"{self.playlist} - {self.video}"
