# myapp/urls.py
from django.urls import path 
from . import views 

# app_name = 'myapp'
urlpatterns = [ 

    path('say_hello/', views.say_hello, name='say_hello'),
    path('display_date/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
    path('homepage/', views.homepage, name='homepage'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('query', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems), 
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
    path('application', views.new_view, name='ApplicationForm'),
    path('', views.home_view, name='index'),  # Root URL only points to 'home_view'
    # path('home', views.form_view),
    path('about/', views.about), #Since this is step 2, check views for step 1, and now go to check the templates folder is in settings.py
    path('home/', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),  
]

