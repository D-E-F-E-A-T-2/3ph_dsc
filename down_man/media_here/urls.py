from .views import testing, MediaInfoViewSet
from django.urls import path, include

urlpatterns = [
    path('', testing),
    path('MediaInfoViewSet/<pk>', MediaInfoViewSet.as_view()),

]
