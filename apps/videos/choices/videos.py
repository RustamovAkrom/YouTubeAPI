from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class NotificationType(TextChoices):
    LIKE = "like", _("Like")
    COMMENT = "comment", _("Comment")
    SUBSCRIPTION = "subscription", _("Subscription")
    VIDEO_UPLOAD = "video_upload", _("Video Upload")
    VIDEO_DELETE = "video_deleted", _("Video Deleted")
    