from celery import shared_task
from apps.videos.models import WatchHistory, Video
from apps.users.models import User


@shared_task
def create_watch_history_task(user_id, video_id):
    user = User.objects.get(id=user_id)
    video = Video.objects.get(id=video_id)
    history = WatchHistory.objects.create(user=user, video=video)
    print(history)
    return history.id
