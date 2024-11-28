from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    return HttpResponse("<h1>404 Pagina no encontrada</h1><br><button onclick"" href'';"">Go to home page</button>")

def home(request):
    return HttpResponseNotFound("<h1>404 no encontrada with responsenotfound</h1>") 