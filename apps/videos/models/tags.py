from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.shared.models import TimestampedModel


class Tag(TimestampedModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        db_table = "tags"
    
    def __str__(self):
        return self.name
