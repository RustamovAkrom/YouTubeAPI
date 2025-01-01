from celery import shared_task
from django.core.mail import send_mail
from apps.users.models import User
from apps.videos.models import Notification
from .emails import send_email_task


@shared_task
def create_notification_task(user_id, message):
    user = User.objects.get(id=user_id)
    notification = Notification.objects.create(user=user, message=message)

    send_email_task.delay(user.email, "YouTube notifications", message)
    return notification.id
