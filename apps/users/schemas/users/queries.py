import graphene
from apps.users.schemas.users.types import UserType
from apps.users.models import User


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    users = graphene.List(UserType, first=graphene.Int(), skip=graphene.Int())

    def resolve_users(self, info, first=None, skip=None):
        qs = User.objects.all()
        if skip:
            qs = qs[skip:]
        if first:
            qs = qs[:first]
        return qs

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

__all__ = ("Query",)
