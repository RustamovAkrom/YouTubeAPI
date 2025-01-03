import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()


from apps.videos.services import (
    get_recomendations, 
    get_recomendations_from_history, 
    get_recomendations_with_dislike_exclusion, 
    get_recomendations_with_dislikes
)

from apps.users.models import User


user = User.objects.last()

print(get_recomendations(user))
print("*" * 30)
print(get_recomendations_from_history(user))
print("*" * 30)
print(get_recomendations_with_dislikes(user))
print("*" * 30)
print(get_recomendations_with_dislike_exclusion(user))
print("*" * 30)