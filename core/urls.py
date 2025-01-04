from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from apps.users.views import PrivateGraphQLView
from apps.videos import consumers


urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("graphql/", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
