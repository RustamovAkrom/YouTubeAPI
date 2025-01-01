from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("rosetta/", include("rosetta.urls")),
    path("graphql/", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
