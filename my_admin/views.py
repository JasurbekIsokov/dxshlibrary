from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import *
from library.models import *
from organization.models import *

def get_all_data():
    libraries = Library.objects.all()
    lib_count = libraries.count()
    organizations = Organization.objects.all()
    org_count = organizations.count()
    news = New.objects.all()
    news_count = news.count()
    contacts = Contact.objects.all()
    con_count = contacts.count()
    contracts = Contract.objects.all()
    contract_count = contracts.count()

    return {
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

# Create your views here.
def home_admin(request):
    return render(request, "my_admin/admin_home.html", get_all_data())

def libraries(request):
    return render(request, "my_admin/admin_library.html", get_all_data())

def organizations(request):
    return render(request, "my_admin/admin_organization.html", get_all_data())

def contracts(request):
    return render(request, "my_admin/admin_contract.html", get_all_data())

def contacts(request):
    return render(request, "my_admin/admin_contact.html", get_all_data())

def news(request):
    return render(request, "my_admin/admin_news.html", get_all_data())