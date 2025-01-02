from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from apps.users.models import User
from apps.videos.models import Notification
from apps.videos.choices import NotificationType
from .emails import send_email_task


logger = get_task_logger(__name__)


@shared_task
def create_notification_task(
    user_id, 
    notification_type, 
    message, 
    related_object_id = None,
    sender_id = None, 
):  
    print("Create notification task")
    try:
        notification = Notification()

        if sender_id is not None:
            sender = User.objects.get(id=sender_id)
            notification.sender = sender

        if related_object_id is not None:
            notification.related_object_id = related_object_id

        user = User.objects.get(id=user_id)

        notification.user = user
        notification.notification_type = notification_type
        notification.message=message
        notification.save()

        logger.info("Notification created successfully.")

    except User.DoesNotExist as e:
        logger.info(f"User dos not exist in create_notification_task: {e}")
        print(f"User not found: {e}")

    except Exception as e:
        logger.info(f"Error in create_notification_task: {e}")
        print(f"An error occurred: {e}")
