from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.conf import settings

import graphene
import graphql_jwt
import graphql_jwt.utils
from graphql_jwt.decorators import login_required
from graphene_file_upload.scalars import Upload
import jwt

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
    

class DeleteUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    success = graphene.Boolean()\
    
    @login_required
    def mutate(self, root, user_id):
        # # check authorization
        # user = info.context.user
        # if not user.is_authenticated:
        #     raise ValidationError("Authorization required.")
        
        try:
            user_to_delete = User.objects.get(id=user_id)
            user_to_delete.delete()
            return DeleteUser(success=True)
        
        except User.DoesNotExist:
            raise Exception("User not found.")
        
 
class UpdateProfile(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        email = graphene.String()
        avatar = Upload()

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, root, email=None, first_name=None, last_name=None, username=None, avatar=None):
        print(root)
        user = root.context.user
        # print(user)

        if username:
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already exists.")
            user.email = email
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists.")
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if avatar:
            user.avatar = avatar

        user.save()
        return UpdateProfile(user=user)
    

class Mutation(graphene.ObjectType):
    """
    Users mutation class
    """
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()

    delete_user = DeleteUser.Field()
    update_profile = UpdateProfile.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field() # Из готовой библиотеки
    verify_token = graphql_jwt.Verify.Field() # Проверка токена
    refresh_token = graphql_jwt.Refresh.Field() # Обновление токена


__all__ = ("Mutation", )
