from graphene_django.types import DjangoObjectType
from apps.users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'avatar', 
            'is_active', 
            'is_staff', 
            'is_superuser'
        ]
