import graphene
from apps.users.schemas.users.types import UserType
from apps.users.models import User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        return User.objects.all()


__all__ = ("Query", )