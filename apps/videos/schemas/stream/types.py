import graphene
from graphene_django.types import DjangoObjectType

from apps.videos.models import LiveStream


class LiveStreamType(DjangoObjectType):
    class Meta:
        model = LiveStream
