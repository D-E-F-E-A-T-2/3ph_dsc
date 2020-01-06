from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PersonSerializer
from rest_framework import generics
from .models import Person
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser


def index(self):
    return HttpResponse("ok")


class PersonListPost(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListShow(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListDelete(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListPut(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = (MultiPartParser, FormParser, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        datafile=self.request.data.get('datafile'))
# curl -X GET http://127.0.0.1:8000/api/v1/friends/ -H 'Authorization: Token d9832a41149d42419818a1ea833ca707c5faca7d' [{"name":"Kush"}]
