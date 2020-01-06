from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import MediaInfoSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from .models import MediaInfo
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
# Create your views here.


def testing(self):
    return HttpResponse("<H1>Media endpoint welcomes you</H1>")

# class MediaInfoViewSet(ModelViewSet):
#     queryset = MediaInfo.objects.all()
#     serializer_class = MediaInfoSerializer
#     parser_classes = (MultiPartParser, FormParser, )

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user,
#                         datafile=self.request.data.get('datafile'))


class MediaInfoViewSet(generics.ListAPIView):
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    queryset = MediaInfo.objects.all()
    serializer_class = MediaInfoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.IsAdminUser, ]


# http: // 127.0.0.1: 8000/media/MediaInfoViewSet/song1
