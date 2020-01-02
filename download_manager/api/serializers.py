from rest_framework import serializers
from .models import Person, Media, DownloadingDetails


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email', 'password']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['media_name', 'media_type', 'playbacks']


class DownloadingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadingDetails
        fields = ['download_count']
