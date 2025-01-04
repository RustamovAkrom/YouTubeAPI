from django.core.exceptions import ValidationError
from django.conf import settings

import graphene
import jwt

from apps.users.models import User


class LoginUser(graphene.Mutation):
    """
    Authorizations
    """

    token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    
    def mutate(self, root, email, password):
        user = User.objects.filter(email=email).first()
        if user is None:
            raise ValidationError("User not found.")
        
        if not user.is_active:
            raise ValidationError("User account is not active.")
        
        if not user.check_password(password):
            raise ValidationError("Password is not correct.")
        
        # token = graphql_jwt.utils.jwt_encode(user)
        payload = {
            "user_id": user.id,
            "email": user.email
        }
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm="HS256"
        )

        return LoginUser(token=token)

__all__ = ("LoginUser", )
