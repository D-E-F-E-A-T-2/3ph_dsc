from .views import testing, DownloadListPost, DownloadListShow
from django.urls import path, include

urlpatterns = [
    path('', testing),
    path('DownloadListPost', DownloadListPost.as_view()),
    path('DownloadListShow', DownloadListShow.as_view()),

]