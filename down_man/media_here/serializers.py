from rest_framework import serializers
from .models import MediaInfo


class MediaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaInfo
        fields = ('media_name', 'media_size', 'datafile')
