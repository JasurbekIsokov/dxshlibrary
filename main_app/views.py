from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from library.models import *
from organization.models import *
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import *


class HomeView(TemplateView):
    template_name = 'main_app/index.html'

    # for middleware
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('my_admin:home'))
        
        news = New.objects.all()
        events = Event.objects.all()
        context = {
            "news": news,
            "events": events,
        }
        return render(request, 'main_app/index.html', context)

    
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                library = Library.objects.filter(user = user)               
                organization = Organization.objects.filter(user = user)

                if library and not library[0].is_active:
                    message = 'Foydalanuvchi faolsizlantirilgan'
                    return render(request, 'main_app/login.html', {'message': message})
                
                if organization and not organization[0].is_active:
                    message = 'Foydalanuvchi faolsizlantirilgan'
                    return render(request, 'main_app/login.html', {'message': message})

                login(request, user)
                if MyAdmin.objects.filter(user = user):
                    return HttpResponseRedirect(reverse('my_admin:home'))
                return HttpResponseRedirect(reverse('home'))
            else:
                message = 'Foydalanuvchi faolsizlantirilgan'
                return render(request, 'main_app/login.html', {'message': message})
        else:
            message = 'Foydalanuvchi nomi yoki parol xato!'
            return render(request, 'main_app/login.html', {'message': message})

    else:
        return render(request, "main_app/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class NewsView(TemplateView):
    # for middleware
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if MyAdmin.objects.filter(user=request.user):
                return HttpResponseRedirect(reverse('my_admin:home'))
        news = New.objects.all()
        return render(request, "main_app/news.html", {"news": news})


class DetailNew(DetailView):
    context_object_name = 'news'
    model = New
    template_name = "main_app/single_news.html"


def contact(request):
    # for middleware
    if request.user.is_authenticated:
        if MyAdmin.objects.filter(user=request.user):
            return HttpResponseRedirect(reverse('my_admin:home'))

    message = ''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        title = request.POST.get('title')
        body = request.POST.get('body')
        Contact.objects.create(
            name=name,
            email=email,
            phone = phone,
            title=title,
            body=body
        )
      
        message = "Xabaringiz yuborildi!"
        return render(request,  'main_app/contact.html',{'message': message})

    return render(request, "main_app/contact.html")