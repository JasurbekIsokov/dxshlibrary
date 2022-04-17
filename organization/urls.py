from django.urls import path
from .views import *

app_name = 'organization'
urlpatterns = [
    path("profile/", profile, name='profile'),
    path("register/", register, name='register'),
]