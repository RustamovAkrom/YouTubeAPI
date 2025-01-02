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
    sender_id, 
    notification_type, 
    message, 
    related_object_id
):  
    print("Create notification task")
    try:
        user = User.objects.get(id=user_id)
        sender = User.objects.get(id=sender_id)
        
        Notification.objects.get_or_create(
            user=user,
            sender=sender,
            notification_type=notification_type,
            message=message,
            related_object_id=related_object_id
        )

        logger.info("Notification created successfully.")

    except User.DoesNotExist as e:
        logger.info(f"User dos not exist in create_notification_task: {e}")
        print("User not found: " + e)

    except Exception as e:
        logger.info(f"Error in create_notification_task: {e}")
        print(f"An error occurred: {e}")
