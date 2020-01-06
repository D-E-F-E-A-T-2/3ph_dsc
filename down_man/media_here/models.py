from django.db import models

# media name:char, media size:int


class MediaInfo(models.Model):
    media_name = models.CharField(max_length=40, primary_key=True)
    media_size = models.IntegerField()
    datafile = models.FileField(blank=True)
    #created_on = models.DateTimeField(auto_now_add=True)
