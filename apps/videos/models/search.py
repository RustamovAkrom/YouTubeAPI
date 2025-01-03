from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class SearchHistory(TimestampedModel):
    user = models.ForeignKey("users.User", models.CASCADE, related_name="search_histories")
    query = models.CharField(max_length=250)

    class Meta:
        verbose_name = _("Search History")
        verbose_name_plural = _("Search Histories")
        ordering = ['-created_at']
        db_table = "search_histories"

    def __str__(self):
        return f"{self.user} - {self.query}"
