import graphene

from apps.videos.models import Channel
from .types import ChannelType


class Query(graphene.ObjectType):
    channels = graphene.List(ChannelType)
    channel_by_id = graphene.Field(ChannelType, id=graphene.Int(required=True))

    def resolve_channels(self, info):
        return Channel.objects.all()
    
    def resolve_channel_by_id(self, info, id):
        try:
            return Channel.objects.filter(id=id)
        except Channel.DoesNotExist:
            return None

__all__ = ("Query", )
