import graphene

from apps.users.schemas import (
    Mutation as UserMutation, 
    Query as UserQuery,
)


class Query(UserQuery):
    pass


class Mutation(UserMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
