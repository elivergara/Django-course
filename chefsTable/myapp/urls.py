# myapp/urls.py
from django.urls import path 
from . import views 

app_name = 'myapp'
urlpatterns = [ 
    path('home/', views.home, name='home'), 
    path('say_hello/', views.say_hello, name='say_hello'),
    path('display_date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
    path('homepage/', views.homepage, name='homepage'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems), 
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
]
