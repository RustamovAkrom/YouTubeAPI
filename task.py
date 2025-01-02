import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

from apps.videos.tasks import create_notification_task

create_notification_task(
    1, 1, "public", "message notification", 1
)
