from django.urls import path
from main_app.views import DetailNew, HomeView, NewsView,  contact, user_login, user_logout
from .models import *

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("login/", user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    path("news/", NewsView.as_view(), name='news'),
    path("simple_new/<str:pk>/", DetailNew.as_view(), name='simple_new'),
    path("contact/", contact, name='contact')
]