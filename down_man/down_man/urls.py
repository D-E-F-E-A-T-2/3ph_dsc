from django.contrib import admin
from django.urls import path, include
from auth123 import urls as auth_url
from media_here import urls as media_url
from usage_database import urls as usage_url
from .views import testing

urlpatterns = [
    path('', testing),
    path('admin/', admin.site.urls),
    path('auth/', include(auth_url)),
    path('media/', include(media_url)),
    path('downloads/', include(usage_url)),
]
