import graphene

from apps.videos.models import Channel
from apps.users.permissions import IsAuthenticatedPermission, IsOwnerPermission



class DeleteChannel(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        user = info.context.user
        
        IsAuthenticatedPermission().has_permission(info.context)
        IsOwnerPermission().has_permission(info.context, user.id)

        try:
            channel = Channel.objects.get(id=id, owner=user)
            channel.delete()
            return DeleteChannel(success=True)
        except Channel.DoesNotExist:
            raise Exception("Channel not found or not owned by you!")

__all__ = ("DeleteChannel", )
