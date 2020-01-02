from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.testing),
    #path('PersonListCreate/', views.PersonListCreate.as_view()),
    #path('PersonListShow/', views.PersonListShow.as_view()),
    #path('PersonViewSet/<pk>', views.PersonViewSet),
    path('AddMedia/', views.AddMedia.as_view()),
    path('ShowMedia/<pk>', views.ShowMedia.as_view()),

]
