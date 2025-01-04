from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

import graphene

from apps.users.schemas.users.types import UserType
from apps.users.models import User


class RegisterUser(graphene.Mutation):
    """
    Registrations
    """

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        date_of_berthd = graphene.Date()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        password_confirm = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, root, first_name, last_name, date_of_berthd, email, password, password_confirm):
        if User.objects.filter(email=email).exists():
            return ValidationError("A user with this email already exists")

        if password != password_confirm:
            # return RegisterUser(user=None, error="Password is not match.") 
            raise ValidationError("Password is not match.")
        try:
            validate_password(password)

            user = User(
                first_name=first_name,
                last_name=last_name,
                date_of_berthd=date_of_berthd,
                email=email,
                password=make_password(password)
            )
            user.save()
            return RegisterUser(user=user)
        
        except ValidationError as e:
            raise ValidationError(str(e))

__all__ = ("RegisterUser", )
