import graphene
from graphene_file_upload.scalars import Upload


from apps.videos.models import Channel
from apps.users.permissions import IsAuthenticatedPermission, IsOwnerPermission
from apps.videos.schemas.channels.types import ChannelType


class UpdateChannel(graphene.Mutation):
    channel = graphene.Field(ChannelType)

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()
        avatar = Upload()

    def mutate(self, info, id, name=None, description=None, avatar=None):
        user = info.context.user

        IsAuthenticatedPermission().has_permission(info.context)
        IsOwnerPermission().has_permission(info.context, user.id)

        try:
            channel = Channel.objects.get(id=id, owner=user)
        except Channel.DoesNotExist:
            raise Exception("Channel not found or not owned by you!")
        
        if name:
            channel.name = name
        if description:
            channel.description = description
        if avatar:
            channel.avatar = avatar
        channel.save()

        return UpdateChannel(channel=channel)

__all__ = ("UpdateChannel", )
