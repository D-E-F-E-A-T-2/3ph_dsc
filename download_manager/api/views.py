from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Media, DownloadingDetails
from .serializers import PersonSerializer, MediaSerializer, DownloadingDetailsSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import DjangoModelPermissions


def testing(self):
    return HttpResponse("""I will Put all routes here.
    </br>PersonListCreate - To create a user(POST)
    </br>PersonListShow - (GET)See all users, /email for unique view
    </br> 'NO' PersonViewSet - (GET)See all users, /email for unique view""")


# Change of workflow, We were desiging a download manager met with confussions. Now
# we are desiging it for individual only.

"""
class PersonListCreate(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListShow(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [DjangoModelPermissions]



#kill my internet
# class PersonViewSet(ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

"""


class AddMedia(generics.CreateAPIView):
    queryset = Media.objects.values_list('id', 'media_name', 'media_type')
    serializer_class = MediaSerializer


class ShowMedia(generics.RetrieveUpdateAPIView):
    # Media.objects.values_list('media_name', 'media_type', 'playbacks')
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    #lookup_field = 'id'

    # def save(self):
    #     self.playbacks += 1
    #     super(Media, self).save()

    # def get_object(self):
    #     username = self.kwargs["username"]
    #     return get_object_or_404(User, username=username)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
