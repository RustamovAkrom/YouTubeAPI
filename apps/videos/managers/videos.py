from django.db.models import Manager

from apps.videos.querysets.videos import  VideoQuerySet


class VideoManager(Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)
    
    def popular(self):
        return self.get_queryset().popular()
    
    def by_channel(self, channel):
        return self.get_queryset().by_channel(channel)
