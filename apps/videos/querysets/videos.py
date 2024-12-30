from django.db.models import QuerySet


class VideoQuerySet(QuerySet):
    def popular(self):
        return self.filter(views__gt=1000)
    
    def by_channel(self, channel):
        return self.filter(channel=channel)
