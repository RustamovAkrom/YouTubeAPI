import graphene
from graphql_jwt.decorators import login_required

from apps.users.models import User


class DeleteUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    success = graphene.Boolean()
    
    @login_required
    def mutate(self, info, user_id):

        try:
            user_to_delete = User.objects.get(id=user_id)
            user_to_delete.delete()
            return DeleteUser(success=True)
        
        except User.DoesNotExist:
            raise Exception("User not found.")
        
__all__ = ("DeleteUser", )
