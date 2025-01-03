from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class VideoReportTypeChoice(TextChoices):
    COPYRIGHT = "copyright", _("Copyright")
    INAPPROPRIATE_CONTENT = "inappropriate_content", _("Inappropriate Content")
    SPAM = "spam", _("Spam")
    HARASSMENT = "harassment", _("Harassment")
    MISLEADING = "misleading", _("Misleading")
    OTHER = "other", _("Other")
