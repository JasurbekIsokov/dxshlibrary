from django.http import HttpResponse

# Create your views here.
def home_admin(request):
    return HttpResponse("<h1>Home admin</h1>")

def libraries(request):
    return HttpResponse("<h1>Libraries admin</h1>")

def organizations(request):
    return HttpResponse("<h1>Organizations admin</h1>")

def contracts(request):
    return HttpResponse("<h1>Admin contracts</h1>")

def news(request):
    return HttpResponse("<h1>Admin news</h1>")