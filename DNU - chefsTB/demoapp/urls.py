# demoapp/urls.py
from django.urls import path 
from . import views 

# app_name='demoapp'
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('say_hello/', views.say_hello, name='say_hello'),

] 

