from django.db import models
import os
# Create your models here.

def path_and_rename_news(instance, filename):
    upload_to = 'Images/News/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = '{}.{}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class New(models.Model):
    title = models.TextField(max_length=50, unique=True)
    body = models.TextField(max_length=500)
    news_pic = models.ImageField(upload_to=path_and_rename_news, verbose_name="News Picture")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self) -> str:
        return self.title

def path_and_rename_events(instance, filename):
    upload_to = 'Images/Events/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.id:
        filename = '{}.{}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class Event(models.Model):
    title = models.TextField(max_length=50, unique=True)
    body = models.TextField(max_length=500)
    events_pic = models.ImageField(upload_to=path_and_rename_events, verbose_name="News Picture")
    date_added = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=50)

    class Meta:
        ordering = ['-date_added']

    def __str__(self) -> str:
        return self.title

class Contract(models.Model):
    pass

class Contact(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()
   

    def __str__(self) -> str:
        return self.title