import graphene

from apps.videos.models import LiveStream
from apps.users.permissions import IsAuthenticatedPermission
from .types import LiveStreamType


class CreateLiveStream(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        start_time = graphene.DateTime()

    live_stream = graphene.Field(LiveStreamType)

    def mutate(self, info, title, description, start_time):
        IsAuthenticatedPermission().has_permission(info.context)
        user = info.context.user

        live_stream = LiveStream(
            title=title,
            description=description,
            user=user,
            start_time=start_time
        )
        live_stream.save()
        return CreateLiveStream(live_stream=live_stream)
    

class Mutation(graphene.ObjectType):
    create_live_stream = CreateLiveStream.Field()

__all__ = ("Mutation", )
