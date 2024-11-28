from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    path = request.path
    response = HttpResponse("This Works!")
    # return HttpResponse(path, content_type='text/html', charset='utf-8')
    return response


def say_hello(request):
    content2 = "<h2>Now this is the Say Hello code<br> In the myapp App!!!</h2>"
    return HttpResponse(content2)


def homepage(request):
    content3 = "<h2>Welcome to Little Lemon!</h2>"
    return HttpResponse(content3)


def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(f"The date you joined is: {date_joined}")


def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!"""
    return HttpResponse(text)


def pathview(request, name, id): 
    return HttpResponse(f"User Name: {name.title()} User ID: {id}")

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse(f"Name:{name.title()} UserID:{id}")

def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse(f"The entered name was :{name} and the UserID: {id}") 

def menuitems(request, dish):
    items = {
        'pasta':'pasta is a type of noodle',
        'falafel':'falafel are deep fried patties',
        'cheesecake':'cheesecake is a dessert'
    }
    description = items[dish]
    return HttpResponse(f"<span style='display:inline; font-size:2em;'>{dish}:</span> "
                        f"<span style='display:inline; font-size:1.5em;'>{description}</span>")

def  drinks(request, drink_name):
    all_drinks = {
        'mocha':'type of coffee',
        'tea':'type of beverage',
        'lemonade':'type of refreshment',
        'milk':'choice of dairy'
    }
    choice_of_drink = all_drinks[drink_name]
    return HttpResponse(f"<h1>{drink_name}:</h1> <h2>{choice_of_drink}</h2>")