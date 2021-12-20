from django.urls import path

from myApp import views
from .views import *


urlpatterns=[
    path('help',views.help,name='HELP'),
    path('', views.users, name='users'),
]