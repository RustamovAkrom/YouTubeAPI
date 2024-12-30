from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.shared.models import TimestampedModel
from apps.videos.choices import CategoryChoice, VisibilityChoice
from apps.videos.managers import VideoManager


class Video(TimestampedModel):

    class AudioLanguageChoices(models.TextChoices):
        EN = "en", "English"
        RU = "ru", "Russian"
        UZ = "uz", "Uzbek"

    class LicenseChoices(models.TextChoices):
        STANDART = "s", "Standart YouTube License"
        CREATIVE = "c", "Creative Commons"
    
    title = models.CharField(max_length=255, db_index=True, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, db_index=True, verbose_name=_("Description"))
    video_file = models.FileField(
        upload_to="video/file/%Y/%m/%d", 
        verbose_name=_("Video File"),
        validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'webm'])]
    )
    thumbnail = models.ImageField(
        upload_to="video/thumbnails/%Y/%m/%d", 
        blank=True, null=True, 
        verbose_name=_("Thumbnail"), 
        max_length=500
    )
    channel = models.ForeignKey(
        "videos.Channel", 
        models.CASCADE, 
        db_index=True,
        related_name="videos", 
        verbose_name="Channel",
    )
    category = models.CharField(
        max_length=100, 
        choices=CategoryChoice.choices, 
        verbose_name=_("Category")
    )
    tag = models.ManyToManyField("videos.Tag", related_name="videos", verbose_name=_("Tag"), db_index=True)
    duration = models.PositiveIntegerField(help_text="Duration in seconds", verbose_name=_("Duration"))
    visibility = models.CharField(
        max_length=10, 
        choices=VisibilityChoice.choices, 
        default=VisibilityChoice.PUBLIC.value,
        verbose_name=_("Visibility")
    )
    views_count = models.PositiveBigIntegerField(default=0, verbose_name=_("Views Count"))
    comments_enabled = models.BooleanField(default=True, verbose_name=_("Comments Enabled"))
    is_premium = models.BooleanField(default=False, verbose_name=_("Is Premium"))
    related_videos = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True, 
        related_name="related_to",
        verbose_name=_("Related Videos")
    )
    license = models.CharField(
        max_length=20, 
        choices=LicenseChoices.choices,
        default=LicenseChoices.STANDART.value,
        verbose_name=_("License")
    )
    is_age_restricted = models.BooleanField(default=False)
    audio_language = models.CharField(
        max_length=2, 
        choices=AudioLanguageChoices.choices,
        default=AudioLanguageChoices.EN.value,
        verbose_name=_("Audio Language")
    )
    # Custom Video Manager
    objects = VideoManager()

    def like_count(self):
        return self.video_likes.count()
    
    def dislike_count(self):
        return self.video_dislikes.count()
    
    def increment_views(self):
        self.views_count += 1
        self.save()

    @property
    def is_popular(self):
        return self.views_count > 1000
    
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        ordering = ['-created_at']
        db_table = "videos"

    def __str__(self):
        return self.title
    

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
