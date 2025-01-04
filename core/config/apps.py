DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PROJECT_APPS = [
    'apps.shared.apps.SharedConfig',
    'apps.users.apps.UsersConfig',
    'apps.videos.apps.VideosConfig',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'modeltranslation',
    'rosetta',
    'django_graphiql',
    'graphene_django',
    'graphene_file_upload',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'channels',
]
