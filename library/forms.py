from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Library

class UserForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
       # }

        widgets = {
            'username': forms.TextInput(attrs={ 'class': 'form-control' }),
            'password1': forms.TextInput(attrs={ 'class': 'form-control' }),
            'password1': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
class LibraryForm(forms.ModelForm):
    yangi_bino = 'yangi bino'
    tamirlash = 'tamirlash'
    fondni_toldirish = 'fondni to\'ldirish'
    internet = 'internet'
    moddiy_texnik = 'moddiy texnik'

    partnership_types = [
        (yangi_bino, 'Yangi bino qurish'),
        (tamirlash, 'Binoni tamirlash'),
        (fondni_toldirish, 'Fondni to\'ldirish'),
        (internet, 'internet'),
        (moddiy_texnik, 'Moddiy texnik ta\'mirlash')
    ]

    partnership_type = forms.ChoiceField(required=True, choices=partnership_types)

    regions = [
        ('Andijon', 'Andijon viloyati'),
        ('Buxoro', 'Buxoro viloyati'),
        ('Farg\'ona', 'Farg\'ona viloyati'),
        ('Jizzax', 'Jizzax viloyati'),
        ('Namangan', 'Namangan viloyati'),
        ('Navoiy', 'Navoiy viloyati'),
        ('Qoraqolpogiston', 'Qoraqalpog\'iston Respublikasi'),
        ('Qashqadaryo', 'Qashqadaryo viloyati'),
        ('Samarqand', 'Samarqand viloyati'),
        ('Sirdaryo', 'Sirdaryo viloyati'),
        ('Surxondaryo', 'Surxondaryo viloyati'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Toshkent shahri', 'Toshkent shahri'),
        ('Xorazm', 'Xorazm viloyati')
    ]

    region = forms.ChoiceField(required=True, choices=regions)
   
    class Meta():
        model = Library
        fields = ('full_name', 'open_year', 'general_fund', 'number_of_users', 'region','full_address','partnership_type', 'library_pic')
        labels = {
            'full_name':'Kutubxona to\'liq nomi',
            'open_year':'Ochilgan yili', 
            'general_fund': 'Umumiy fondi', 
            'number_of_users': "Foydalanuvchilar soni", 
            'region': 'Viloyati',
            'full_address': "Tuman, Shaharcha, ko\'cha",
            'partnership_type': 'Hamkorlik turi', 
            'library_pic': "Rasm yuklang"
        }