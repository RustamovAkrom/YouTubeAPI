from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.db import models
import secrets


def generate_stream_key():
    return secrets.token_hex(16)


class LiveStream(models.Model):
    STATUS_CHOICES = (
        ('sheduled', _('Sheduled')),
        ('live', _('Live')),
        ('finished', _('Finished')),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey("users.User", models.CASCADE, related_name="streams")
    stream_key = models.CharField(max_length=32, unique=True, default=generate_stream_key) # Authentification field
    video_file = models.FileField(
        upload_to="streams/videos/%Y/%m/%d", 
        verbose_name=_("Video File"),
        validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'webm'])],
        blank=True, 
        null=True
    )
    audio_file = models.FileField(
        upload_to="streams/audios/%Y/%m/%d", 
        verbose_name=_("Audo File"),
        validators=[FileExtensionValidator(['mp3', 'wav', 'flac'])],
        blank=True, 
        null=True
    )
    messages = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="sheduled")
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def get_rtmp_url(self):
        return f"rtmp://127.0.0.1/live/{self.stream_key}"
    
    class Meta:
        verbose_name = _("Live Stream")
        verbose_name_plural = _("Live Streams")
        db_table = _("live_streams")

    def __str__(self):
        return self.title
    