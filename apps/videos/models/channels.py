from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse

from apps.shared.models import TimestampedModel


class Channel(TimestampedModel):
    owner = models.ForeignKey("users.User", models.CASCADE, related_name="channels", verbose_name=_("Owner"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    avatar = models.ImageField(upload_to="channel/avatar/%Y/%m/%d", blank=True, null=True, verbose_name=_("Avatar"))
    subscribers = models.ManyToManyField(
        "users.User",
        symmetrical=False,
        related_name="subscribed_channels",
        verbose_name=_("subscribed"),
        blank=True,
    )
    social_links = models.JSONField(
        verbose_name=_("Social Links"),
        default=dict,
        blank=True,
        null=True,
        help_text="JSON object with links, e.g., {'twiter': 'url', 'instagram': 'url'}"
    )

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")
        ordering = ["-created_at"]
        db_table = "channels"

    def __str__(self):
        return self.name

    def follow(self, user):
        if user != self.owner:
            if not self.subscribers.filter(id=user.id).exists():
                self.subscribers.add(user)
        return "You owner it is channel!"

    def unfollow(self, user):
        if self.subscribers.filter(id=user.id).exists():
            self.subscribers.remove(user)

    def total_subscribers(self):
        return self.subscribers.count()

    def get_avatar(self):
        return self.avatar.url if self.avatar else None

    def videos_count(self):
        return self.videos.count()
    