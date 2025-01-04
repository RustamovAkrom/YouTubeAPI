import graphene

from apps.users.schemas import (
    Mutation as UserMutation, 
    Query as UserQuery,
)
from apps.videos.schemas.channels import (
    Mutation as ChannelMutation,
    Query as ChannelQuery,
)


class Query(
    UserQuery, 
    ChannelQuery
):...


class Mutation(
    UserMutation,
    ChannelMutation,
):...


schema = graphene.Schema(query=Query, mutation=Mutation)
