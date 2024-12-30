from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class PlayList(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="playlists", verbose_name=_("User"))
    channel = models.ForeignKey("videos.Channel", models.CASCADE, related_name="playlists", verbose_name=_("Channel"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    is_public = models.BooleanField(default=False, verbose_name=_("Is Public"))
    
    class Meta:
        verbose_name = _("Play List")
        verbose_name_plural = _("Play Lists")
        ordering = ['-created_at']
        db_table = "playlists"

    def __str__(self):
        return self.name


class PlayListVideo(TimestampedModel):
    playlist = models.ForeignKey("videos.PlayList", models.CASCADE, related_name="playlist_videos", verbose_name=_("PlayList"))
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="playlist_videos", verbose_name=_("Video"))
    
    class Meta:
        verbose_name = _("Play List Video")
        verbose_name_plural = _("Play List Videos")
        ordering = ['-created_at']
        db_table = "playlist_videos"

    def __str__(self):
        return f"{self.playlist} - {self.video}"
