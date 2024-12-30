from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel
from apps.videos.choices import CategoryChoice, VisibilityChoice


class Video(TimestampedModel):

    class AudioLanguageChoices(models.TextChoices):
        EN = "en", "English"
        RU = "ru", "Russian"
        UZ = "uz", "Uzbek"

    class LicenseChoices(models.TextChoices):
        STANDART = "s", "Standart YouTube License"
        CREATIVE = "c", "Creative Commons"
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to="video/file/%Y/%m/%d")
    thumbnail = models.ImageField(upload_to="video/thumbnails/%Y/%m/%d", blank=True, null=True)
    channel = models.ForeignKey("videos.Channel", models.CASCADE, related_name="videos")
    category = models.CharField(max_length=100, choices=CategoryChoice.choices)
    tag = models.ManyToManyField("videos.Tag", related_name="videos")
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    visibility = models.CharField(
        max_length=10, 
        choices=VisibilityChoice.choices, 
        default=VisibilityChoice.PUBLIC.value
    )
    views_count = models.PositiveBigIntegerField(default=0)
    comments_enabled = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    related_videos = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True, 
        related_name="related_to"
    )
    license = models.CharField(
        max_length=20, 
        choices=LicenseChoices.choices,
        default=LicenseChoices.STANDART.value
    )
    is_age_restricted = models.BooleanField(default=False)
    audio_language = models.CharField(
        max_length=2, 
        choices=AudioLanguageChoices.choices,
        default=AudioLanguageChoices.EN.value
    )

    def like_count(self):
        return self.video_likes.count()
    
    def dislike_count(self):
        return self.video_dislikes.count()
    

class VideoLike(models.Model):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="video_likes")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="video_likes")

    class Meta:
        verbose_name = _("Video Like")
        verbose_name_plural = _("Video Likes")
        db_table = "video_likes"

    def __str__(self):
        return f"{self.user} :(liked): {self.video}"


class VideoDislike(models.Model):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="video_dislikes")
    video = models.ForeignKey("videos.Video", models.CASCADE, related_name="video_dislikes")

    class Meta:
        verbose_name = _("Video Dislike")
        verbose_name_plural = _("Video Dislikes")
        db_table = "video_dislikes"

    def __str__(self):
        return f"{self.user} :(disliked): {self.video}"
