import graphene
from graphene_file_upload.scalars import Upload

from apps.videos.models import Channel
from apps.videos.schemas.channels.types import ChannelType
from apps.users.permissions import IsAuthenticatedPermission


class CreateChannel(graphene.Mutation):
    channel = graphene.Field(ChannelType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        avatar = Upload()


    def mutate(self, info, name, description=None, avatar=None):
        user = info.context.user

        IsAuthenticatedPermission().has_permission(info.context)

        channel = Channel.objects.get_or_create(
            owner=user, name=name, description=description, avatar=avatar
        )
        return CreateChannel(channel=channel)

__all__ = ("CreateChannel", )
