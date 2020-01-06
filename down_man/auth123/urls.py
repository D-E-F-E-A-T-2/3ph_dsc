from .views import testing
from django.urls import path, include

urlpatterns = [
    path('nope/', testing),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
