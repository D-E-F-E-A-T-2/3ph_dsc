from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('PersonListCreate/', views.PersonListPost.as_view()),
    path('PersonListShow/', views.PersonListShow.as_view()),
    path('PersonListDelete/<pk>', views.PersonListDelete.as_view()),
    path('PersonListPut/<pk>', views.PersonListPut.as_view()),
    path('PersonViewSet/<pk>', views.PersonViewSet),

    # path('api/, views.),
]
