from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import New, Event, Contact


class HomeView(TemplateView):
    template_name = 'main_app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = New.objects.all()
        events = Event.objects.all()
        context['news'] = news
        context['events'] = events
        return context

    
def user_login(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
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
    template_name = "main_app/news.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = New.objects.all()
        context['news'] = news
        return context


class DetailNew(DetailView):
    context_object_name = 'news'
    model = New
    template_name = "main_app/single_news.html"


def contact(request):
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