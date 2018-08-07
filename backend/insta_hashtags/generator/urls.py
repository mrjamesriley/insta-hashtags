from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
  path('', views.home, name='home'),
  path('add', views.add, name='add')
]