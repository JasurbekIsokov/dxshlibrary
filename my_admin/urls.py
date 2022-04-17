from django.urls import path
from .views import *

app_name = "my_admin"
urlpatterns = [
    path("", home_admin, name='home'),
    path("organization/", organizations, name='organization'),
    path("library/", libraries, name='library'),
    path("contract/", contracts, name='contact'),
    path("news/", news, name='news'),
]