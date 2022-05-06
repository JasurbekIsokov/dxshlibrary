from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Library
from organization.models import Organization
from main_app.models import New, Contract
from django.contrib.auth.models import User

# Create your views here.
class Libraries(TemplateView):
    template_name = "library/library_all.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = Library.objects.all()
        context['libraries'] = news
        return context
    
def profile(request, pk):
    if request.method == "POST":
        help = request.POST.get('help')
        library_id = request.POST.get('library_id')
        organization_id = request.POST.get('organization_id')
        app_file = request.FILES.get('app')

        organization = Organization.objects.get(id=organization_id)
        library = Library.objects.get(id=library_id)

        Contract.objects.create(
            organization = organization,
            library = library,
            help = help,
            app_file = app_file,
        )

        library = Library.objects.get(id=pk)
        news = New.objects.all()
        news = news.reverse()
        contracts = Contract.objects.filter(library=library)
        context = {
            'library':library,
            'news': news,
            'contracts': contracts
        }

        return render(request, 'library/library_profile.html',context)
   
    library = Library.objects.get(id=pk)
    news = New.objects.all()
    news = news.reverse()
    contracts = Contract.objects.filter(library=library)
    context = {
        'library':library,
        'news': news,
        'contracts': contracts
    }
    return render(request, 'library/library_profile.html',context) 

def register(request):
    registered = False
    message = ""

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        year = request.POST.get('year')
        fond = request.POST.get('fond')
        numberUsers = request.POST.get('numberUsers')
        partnership_type = request.POST.get('partnership_type')
        region = request.POST.get('region')
        fullAddress = request.POST.get('fullAddress')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        library_pic = request.FILES.get('library_pic')
        
        if password1 != password2:
            message = "Parolni to'g'ri takrorlang"
            return render(request, 'library/library_register.html',
                            {'registered':registered, 'message':message})
        elif len(password1) < 6:
            message = "Parol 6 ta belgidan kam bo'lmasin"
            return render(request, 'library/library_register.html',
                            {'registered':registered, 'message':message})

        elif User.objects.filter(username=username).exists():
            message = "Foydalanuvchi nomi band"
            return render(request, 'library/library_register.html',
                            {'registered':registered, 'message':message})
        else:
            user = User.objects.create_user(username, 'lennon@thebeatles.com', password1)
            library = Library.objects.create(user=user, 
                                            full_name=fullname, 
                                            open_year=year, 
                                            general_fund = fond,
                                            number_of_users = numberUsers,
                                            full_address = fullAddress,
                                            partnership_type = partnership_type,
                                            region = region,
                                            library_pic = library_pic)
            message = "Ookay"
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'library/library_register.html',
                            {'registered':registered,})
    
