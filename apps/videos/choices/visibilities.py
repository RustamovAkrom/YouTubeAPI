from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class VisibilityChoice(TextChoices):
    PUBLIC = "Public", _("Public")
    PRIVATE = "Private", _("Private")
    UNLISTED = "Unlisted", _("Unlisted")
