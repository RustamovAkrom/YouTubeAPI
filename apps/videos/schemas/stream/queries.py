import graphene

from apps.videos.models import LiveStream
from .types import LiveStreamType


class Query(graphene.ObjectType):
    live_streams = graphene.List(LiveStreamType)

    def resolve_live_streams(self, info):
        return LiveStream.objects.all()

__all__ = ("Query", )
