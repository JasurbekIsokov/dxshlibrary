from django.http import HttpResponseRedirect
from django.urls import reverse
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

def home_admin(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))

    return render(request, "my_admin/admin_home.html", get_all_data())

def libraries(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        id = request.POST.get("id");
        library = Library.objects.get(id=id)
        if library.is_active:
            library.is_active = False
        else:
            library.is_active = True
        library.save()
        
        return HttpResponseRedirect(reverse('my_admin:library'))
    return render(request, "my_admin/admin_library.html", get_all_data())

def organizations(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        id = request.POST.get("id");
        organization = Organization.objects.get(id=id)
        if organization.is_active:
            organization.is_active = False
        else:
            organization.is_active = True
        organization.save()
        
        return HttpResponseRedirect(reverse('my_admin:organization'))
    return render(request, "my_admin/admin_organization.html", get_all_data())

def contracts(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        id = request.POST.get("id");
        contract = Contract.objects.get(id=id)
        value = request.POST.get("value")
        if value == '+':
            contract.state = "Qabul qilindi"
        if value == '-':
            contract.state = "Bekor qilindi"
        
        contract.save()
        return HttpResponseRedirect(reverse('my_admin:contract'))
    return render(request, "my_admin/admin_contract.html", get_all_data())

def contacts(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        id = request.POST.get("id");
        contact = Contact.objects.get(id=id)
        value = request.POST.get("read")
        if value == "O'qildi":
            contact.is_read = True
            contact.save()
        return HttpResponseRedirect(reverse('my_admin:contact'))
    return render(request, "my_admin/admin_contact.html", get_all_data())

def news(request):
    # middleware
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.user.is_authenticated:
            if not MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('home'))
                
    if request.method == "POST":
        id = request.POST.get("id");
        if request.POST.get("value") == "O'chirish":
            New.objects.get(id=id).delete()
        else:
            title = request.POST.get("title")
            body = request.POST.get("body")
            img = request.FILES.get('img')

            New.objects.create(
                title=title,
                body=body,
                news_pic=img
            ).save()

        return HttpResponseRedirect(reverse('my_admin:news'))
    return render(request, "my_admin/admin_news.html", get_all_data())