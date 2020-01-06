from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .models import DownloadInfo
from .serializers import DownloadInfoSerializer

def testing(self):
    return HttpResponse("<H1>Download Stats endpoint welcomes you</H1>")


#post request to post user download info in db
class DownloadListPost(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = DownloadInfo.objects.all()
    serializer_class = DownloadInfoSerializer

#get request to get data of logged in user
# This data will be used for calculating montly and daily downloads of user
# by summing the media_size, and favourite media etc will also be found using this.


class DownloadListShow(generics.ListAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = DownloadInfoSerializer
    def get_queryset(self):
        """
        This view should return a list of all the downloads
        for the currently authenticated user.
        """
        user = self.request.user
        return DownloadInfo.objects.filter(user_email=user.email)