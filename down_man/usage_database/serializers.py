from rest_framework import serializers
from .models import DownloadInfo


class DownloadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadInfo
        fields = ('user_email', 'media_name', 'media_size', 'viewed_on')