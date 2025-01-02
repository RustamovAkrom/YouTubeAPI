# from celery import shared_task
# from apps.videos.models import Video
# from .emails import send_email_task


# @shared_task
# def send_video_upload_notification_task(video_id):
#     try:
#         video = Video.objects.get(id=video_id)
#         subject = "New video on your channel!"
#         message = f"The video '{video.title} ' was successfully uploaded to your channel."
#         send_email_task.delay(video.channel.owner.email, subject, message)

#     except Video.DoesNotExist:
#         print(f"Video ID {video_id} not found.")
    