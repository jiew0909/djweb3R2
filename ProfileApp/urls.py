from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('Hello', views.helloworld, name='hello'),
    path('firstPage', views.firstPage, name="firstPage"),
    path('Secondpage', views.Secondpage, name='Secondpage'),
    path('thirdpahe', views.thirdpahe, name='thirdpahe'),
    path('hnypage', views.hnypage, name='hnypage'),
]
