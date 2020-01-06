from django.db import models

class DownloadInfo(models.Model):
    user_email = models.EmailField(max_length=40)
    media_name = models.CharField(max_length=40, primary_key=True)
    media_size = models.IntegerField()
    viewed_on = models.DateTimeField(auto_now_add=True)