import graphene

from apps.users.schemas import (
    Mutation as UserMutation, 
    Query as UserQuery,
)
from apps.videos.schemas.channels import (
    Mutation as ChannelMutation,
    Query as ChannelQuery,
)
from apps.videos.schemas.stream import (
    Mutation as StreamMutation,
    Query as StreamQuery
)

class Query(
    UserQuery, 
    ChannelQuery,
    StreamQuery,
):...


class Mutation(
    UserMutation,
    ChannelMutation,
    StreamMutation,
):...


schema = graphene.Schema(query=Query, mutation=Mutation)
