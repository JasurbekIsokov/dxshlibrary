from django.urls import path
from .views import *

app_name = 'organization'
urlpatterns = [
    path("profile/<str:pk>/", profile_organization, name='profile'),
    path("register/", register, name='register'),
]