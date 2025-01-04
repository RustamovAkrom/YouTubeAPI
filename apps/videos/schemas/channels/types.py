import graphene
from graphene_django.types import DjangoObjectType
from apps.videos.models import Channel


class ChannelType(DjangoObjectType):
    avatar_url = graphene.String()
    videos_count = graphene.Int()
    social_links = graphene.JSONString()
    avatar_url = graphene.String()

    class Meta:
        model = Channel
        fields = [
            "id",
            "name",
            "description",
            "avatar",
            "avatar_url",
            "social_links",
            "videos_count",
            "owner",
            "subscribers",
        ]

    def resolve_avatar_url(self, info):
        return self.get_avatar()

    def resolve_videos_count(self, info):
        return self.videos_count()
