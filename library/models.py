from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
def path_and_rename_library(instance, filename):
    upload_to = 'Images/Library/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = '{}.{}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class Library(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, default='library')
    full_name = models.CharField(max_length=255)
    open_year = models.IntegerField()
    general_fund = models.IntegerField()
    number_of_users = models.IntegerField()
    full_address = models.TextField()

    yangi_bino = 'yangi bino'
    tamirlash = 'tamirlash'
    fondni_toldirish = 'fondni to\'ldirish'
    internet = 'internet'
    moddiy_texnik = 'moddiy texnik'

    is_active = models.BooleanField(default=True)
    
    partnership_types = [
        (yangi_bino, 'Yangi bino qurish'),
        (tamirlash, 'Binoni tamirlash'),
        (fondni_toldirish, 'Fondni to\'ldirish'),
        (internet, 'internet'),
        (moddiy_texnik, 'Moddiy texnik ta\'mirlash')
    ]

    partnership_type = models.CharField(max_length=50, choices=partnership_types, default=yangi_bino)

    regions = [
        ('Andijon', 'Andijon viloyati'),
        ('Buxoro', 'Buxoro viloyati'),
        ('Farg\'ona', 'Farg\'ona viloyati'),
        ('Jizzax', 'Jizzax viloyati'),
        ('Namangan', 'Namangan viloyati'),
        ('Navoiy', 'Navoiy viloyati'),
        ('Qoraqolpog\'iston', 'Qoraqalpog\'iston Respublikasi'),
        ('Qashqadaryo', 'Qashqadaryo viloyati'),
        ('Samarqand', 'Samarqand viloyati'),
        ('Sirdaryo', 'Sirdaryo viloyati'),
        ('Surxondaryo', 'Surxondaryo viloyati'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Toshkent shahri', 'Toshkent shahri'),
        ('Xorazm', 'Xorazm viloyati')
    ]

    region = models.CharField(max_length=70, choices=regions)
    library_pic = models.ImageField(upload_to=path_and_rename_library, verbose_name="Library Picture")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
