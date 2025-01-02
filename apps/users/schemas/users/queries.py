import graphene
from apps.users.schemas.users.types import UserType
from apps.users.models import User


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)


__all__ = ("Query",)
