from django.db.models import TextChoices


class VisibilityChoice(TextChoices):
    PUBLIC = "Public"
    PRIVATE = "Private"
    UNLISTED = "Unlisted"
