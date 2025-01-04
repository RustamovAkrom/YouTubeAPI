from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('graphql/', consumers.VideoChatConsumer.as_asgi()),
]
