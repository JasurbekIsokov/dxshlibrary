from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Organization
from main_app.models import MyAdmin, New, Contract
from library.models import Library

# Create your views here.

def profile_organization(request, pk=None):
    organization = Organization.objects.get(id=pk)
    contracts = Contract.objects.filter(organization=organization)
    news = New.objects.all()
    news = news.reverse()
    
    context = {
        'organization': organization,
        'news': news,
        'contracts': contracts
    }
    return render(request, 'organization/organization_profile.html',context) 


def register(request):
    # for middleware
    if request.user.is_authenticated:
        if MyAdmin.objects.filter(user=request.user):
            return HttpResponseRedirect(reverse('my_admin:home'))
        return HttpResponseRedirect(reverse('home'))
            
    registered = False
    message = ""

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        year = request.POST.get('year')
        phone = request.POST.get('phone')
        organization_type = request.POST.get('organization_type')
        region = request.POST.get('region')
        fullAddress = request.POST.get('fullAddress')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        organization_pic = request.FILES.get('organization_pic')
        
        if password1 != password2:
            message = "Parolni to'g'ri takrorlang"
            return render(request, 'organization/organization_register.html',
                            {'registered':registered, 'message':message})
        elif len(password1) < 6:
            message = "Parol 6 ta belgidan kam bo'lmasin"
            return render(request, 'organization/organization_register.html',
                            {'registered':registered, 'message':message})

        elif User.objects.filter(username=username).exists():
            message = "Foydalanuvchi nomi band"
            return render(request, 'organization/organization_register.html',
                            {'registered':registered, 'message':message})
        
        elif Organization.objects.filter(full_name=fullname).exists():
            message = "Bu tashkilot allaqachon mavjud"
            return render(request, 'organization/organization_register.html',
                            {'registered':registered, 'message':message})
        
        elif Organization.objects.filter(full_address=fullAddress).exists():
            message = "Bu hudud allaqachon mavjud"
            return render(request, 'organization/organization_register.html',
                            {'registered':registered, 'message':message})
        
        else:
            user = User.objects.create_user(username, 'lennon@thebeatles.com', password1)
            organization = Organization.objects.create(user=user, 
                                            full_name=fullname, 
                                            open_year=year, 
                                            phone = phone,
                                            organization_type = organization_type,
                                            full_address = fullAddress,
                                            region = region,
                                            organization_pic = organization_pic)
            message = "Ookay"
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'organization/organization_register.html',
                            {'registered':registered, "message":message})
    

