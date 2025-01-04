from .delete import * # noqa
from .login import * # noqa
from .register import * # noqa
from .update_profile import * # noqa
from ..google.mutations import GoogleAuthMutation

import graphql_jwt
import graphene


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

    google_auth = GoogleAuthMutation.Field()

__all__ = ("Mutation", )
