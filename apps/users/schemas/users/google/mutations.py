import graphene
import requests
from apps.users.models import User
from apps.users.schemas.users.types import UserType


class GoogleAuthMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)
    message = graphene.String()

    def mutate(self, info, token):
        google_api_url = "https://oauth2.googleapis.com/tokeninfo"
        response = requests.get(google_api_url, params={"id_token": token})
        if response.status_code != 200:
            raise Exception("Invalid Google Token.")
        
        data = response.json()
        email = response.get("email")
        name = data.get("name")

        if not email:
            raise Exception("Google response mussing email.")
        
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.username = name
            user.save()
        
        return GoogleAuthMutation(user=user, message="Authentication successful.")
