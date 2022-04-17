from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
def path_and_rename_organization(instance, filename):
    upload_to = 'Images/Organization/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = '{}.{}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, default='organization')
    full_name = models.CharField(max_length=255)
    open_year = models.IntegerField()
    full_address = models.TextField()
    phone = models.CharField(max_length=20)
    organization_type = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
   
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
    organization_pic = models.ImageField(upload_to=path_and_rename_organization, verbose_name="Organization Picture")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
