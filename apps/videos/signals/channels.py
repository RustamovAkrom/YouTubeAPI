from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from apps.videos.models import Channel, NotificationType
from apps.videos.tasks import create_notification_task


@receiver(m2m_changed, sender=Channel.subscribers.through)
def create_subscription_notification(sender, instance, action, reverse, model, pk_set, **kwargs):
    print("Create subscription notification")
    if action == "post_add":
        for user_id in pk_set:
            create_notification_task.delay(
                user_id=user_id,
                sender_id=instance.owner.id,
                notification_type=NotificationType.SUBSCRIPTION,
                message=f'Вы подписались на канал "{instance.name}".',
                related_object_id=instance.id,
            )
