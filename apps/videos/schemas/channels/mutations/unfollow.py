import graphene
from graphene_file_upload.scalars import Upload

from apps.videos.models import Channel
from apps.videos.schemas.channels.types import ChannelType
from apps.users.permissions import IsAuthenticatedPermission


class UnsubscribeFromChannel(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        channel_id = graphene.Int(required=True)

    def mutate(self, info, channel_id):
        user = info.context.user

        IsAuthenticatedPermission().has_permission(info.context)

        try:
            channel = Channel.objects.get(id=channel_id)
            channel.unfollow(user)
            return UnsubscribeFromChannel(success=True)
        
        except Channel.DoesNotExist:
            raise Exception("Channel not found!")

__all__ = ("UnsubscribeFromChannel",)
