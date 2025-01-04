from django.core.exceptions import ValidationError

import graphene
from graphene_file_upload.scalars import Upload

from apps.users.schemas.users.types import UserType
from apps.users.models import User
from apps.users.permissions import IsOwnerPermission


class UpdateProfile(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        email = graphene.String()
        avatar = Upload()

    user = graphene.Field(UserType)

    def mutate(self, info, user_id, email=None, first_name=None, last_name=None, username=None, avatar=None):
        user = info.context.user
        
        # Permissions
        IsOwnerPermission().has_permission(info.context, user_id)
        
        profile_user = User.objects.get(id=user_id)

        if username:
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already exists.")
            profile_user.username = username
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists.")
            profile_user.email = email
        
        profile_user.first_name = first_name or profile_user.first_name
        profile_user.last_name = last_name or profile_user.last_name
        profile_user.username = username or profile_user.username
        profile_user.email = email or profile_user.email

        if avatar:
            user.avatar = avatar

        user.save()
        return UpdateProfile(user=user)
    
__all__ = ("UpdateProfile",)
