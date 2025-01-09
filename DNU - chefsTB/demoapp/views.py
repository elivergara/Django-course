from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request):
    path = request.path
    method = request.method
    content = content = f""" 
                            <center><h2>Testing Django Request Response Objects</h2> 
                            <p>Request path : "{path}"</p> 
                            <p>Request Method : {method}</p></center> """

    return HttpResponse(content)

def say_hello(request):
    content2 = "<h2>Now this is the Say Hello code<br> In the demoapp App!!!</h2>"
    return HttpResponse(content2)
