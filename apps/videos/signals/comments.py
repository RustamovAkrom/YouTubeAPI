from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.videos.models import Comment, NotificationType
from apps.videos.tasks import create_notification_task, send_email_task


@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    print("Comment notification...")
    if created:
        video_owner = instance.video.channel.owner
        if video_owner != instance.user:
            create_notification_task.delay(
                user_id=video_owner.id,
                sender_id=instance.user.id,
                notification_type=NotificationType.COMMENT,
                message=f"{instance.user.username} оставил комментарий на ваше видео '{instance.video.title}'",
                related_object_id=instance.id
            )

            send_email_task.delay(
                to_emails=[video_owner.email],
                from_email=instance.user.email,
                subject="Новый комментарий на ваше видео",
                message=(
                    f"Пользователь {instance.user.username} оставил комментарий на ваше видео '{instance.video.title}'.\n\n"
                    f"Комментарий: {instance.message}\n"
                    f"Ссылка на видео: https://example.com/videos/{instance.video.id}/"                )
            )
