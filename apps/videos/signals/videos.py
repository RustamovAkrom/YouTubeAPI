from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver
from apps.videos.models import Video
from apps.videos.choices import NotificationType, VisibilityChoice
from apps.videos.tasks import create_notification_task, send_email_task


@receiver(post_save, sender=Video)
def video_uploaded_notification(sender, instance, created, **kwargs):
    print("Video Upload notification task")
    # if created:
    if instance.visibility != VisibilityChoice.PRIVATE:

        subscribers = instance.channel.subscribers.all()
        for subscriber in subscribers:
            print(f"Notification for {subscriber.id} is being sent")
            subject = "YouTube: new message"
            message = f"{instance.channel.owner.username} загрузил новое видео: {instance.title}"
            create_notification_task.delay(
                user_id=subscriber.id,
                sender_id=instance.channel.owner.id,
                notification_type=NotificationType.VIDEO_UPLOAD,
                message=message,
                related_object_id=instance.id,
            )
            to_email = subscriber.email
            from_email = instance.channel.owner.email

            send_email_task.delay(
                to_email=to_email,
                from_email=from_email,
                subject=subject,
                message=message,
            )
                
                
