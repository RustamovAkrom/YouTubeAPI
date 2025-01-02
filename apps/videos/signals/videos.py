from django.db.models.signals import post_save, post_delete
from django.db import transaction
from django.dispatch import receiver
from apps.videos.models import Video
from apps.videos.choices import NotificationType, VisibilityChoice
from apps.videos.tasks import create_notification_task, send_email_task
from django.conf import settings


@receiver(post_save, sender=Video)
def video_uploaded_notification(sender, instance, created, **kwargs):
    # if created:
        if instance.visibility != VisibilityChoice.PRIVATE:

            subject = "YouTube: Новое видео!"
            message = f"Канал {instance.channel.name} загрузил новое видео: {instance.title}."
            from_email = instance.channel.owner.email

            subscribers = instance.channel.subscribers.all()
            subscribers_email = [s.email for s in subscribers if s.email]

            for subscriber in subscribers:
                create_notification_task.delay(
                    user_id=subscriber.id,
                    sender_id=instance.channel.owner.id,
                    notification_type=NotificationType.VIDEO_UPLOAD,
                    message=message,
                    related_object_id=instance.id,
                )

            if subscribers_email:
                send_email_task.delay(
                    to_emails=subscribers_email,
                    from_email=from_email,
                    subject=subject,
                    message=message,
                )
                

@receiver(post_delete, sender=Video)
def video_deleted_notification(sender, instance, **kwargs):
    create_notification_task.delay(
        user_id=instance.channel.owner.id,
        notification_type=NotificationType.VIDEO_DELETE,
        message=f'Video "{instance.title}" is deleted',
        related_object_id=None,
        sender_id=None,
    )
    
    send_email_task.delay(
        to_emails=[instance.channel.owner.email],
        from_email=settings.EMAIL_HOST_USER,
        subject="Video deleted",
        message=f'Video "{instance.title}" is deleted.',
    )

