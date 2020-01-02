from django.db import models

# person will later be used for registration and \
# singin


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    password = models.CharField(max_length=10)


class Media(models.Model):
    media_name = models.CharField(max_length=30)
    media_type = models.CharField(max_length=20)
    playbacks = models.IntegerField(default=1, blank=True, null=True)


# user download count
# complexity increases when we are storingp media names and media download dates
# along with user specific downloads.
# for now we will be increasing it's count whenever a request is sended on it's api
class DownloadingDetails(models.Model):
    download_count = models.IntegerField(default=1, blank=True, null=True)
