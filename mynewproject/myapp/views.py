from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import DemoForm, ApplicationForm, LogForm, CustomerForm


# def home(request):
#     path = request.path
#     response = HttpResponse("This Works!")
#     # return HttpResponse(path, content_type='text/html', charset='utf-8')
#     return response


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

def home_view(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'success.html')
    else:
        form = DemoForm()

    return render(request, 'form.html', {'form': form})


def new_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            print(form.cleaned_data)  # Debugging output
            return render(request, 'success.html')
        else:
            print(form.errors)  # Debugging output
    else:
        form = ApplicationForm()

    return render(request, 'form.html', {'form': form})



def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()    
    context = {'form': form}
    return render(request, 'form.html', context)

def cust_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()    
    context = {'form': form}
    return render(request, 'form.html', context)



from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu


def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 

# Create your views here for menu.



def home(request): 
    return render(request, "partial/index.html", {}) 

def about(request):
    about_content = {'about':'Based in Chicago, IL, Little Lemon is a small business that specializes in coffee and tea.'}
    return render(request, "partial/about.html", about_content) #Step 1 make the View, now go to urls.py

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}  # Create a dictionary to pass to the template
    return render(request, 'partial/menu.html', items_dict)  # Pass the dictionary to the template


