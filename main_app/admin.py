from django.contrib import admin
from .models import Contact, New, Event
# Register your models here.
admin.site.register(New)
admin.site.register(Event)
admin.site.register(Contact)