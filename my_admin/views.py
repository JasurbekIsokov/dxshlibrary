from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import *
from library.models import *
from organization.models import *

# Create your views here.
def home_admin(request):
    libraries = Library.objects.all()
    lib_count = libraries.count()
    organizations = Organization.objects.all()
    org_count = organizations.count()
    news = New.objects.all()
    news_count = news.count()
    contacts = Contact.objects.all()
    con_count = contacts.count()
    contracts = Contract.objects.all()
    contract_count = contacts.count()

    context = {
        "libraries":libraries,
        "lib_count":lib_count,
        "organizations":organizations,
        "org_count":org_count,
        "news":news,
        "news_count":news_count,
        "contacts":contacts,
        "contact_count":con_count,
        "contracts":contracts,
        "contract_count":contract_count
    }
    return render(request, "my_admin/admin_home.html", context)

def libraries(request):
    return HttpResponse("<h1>Libraries admin</h1>")

def organizations(request):
    return HttpResponse("<h1>Organizations admin</h1>")

def contracts(request):
    return HttpResponse("<h1>Admin contracts</h1>")

def news(request):
    return HttpResponse("<h1>Admin news</h1>")