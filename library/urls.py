from django.urls import path
from .views import *

app_name = "library"

urlpatterns = [
    path("", Libraries.as_view(), name='home'),
    path("profile/<str:pk>/", profile, name='profile'),
    path("register/", register, name='register'),
] 