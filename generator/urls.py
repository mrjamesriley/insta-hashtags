from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login, logout
from generator.views import AddCategoryOrHashtag



urlpatterns = [
    path('', views.home, name='home'),
    path('add', AddCategoryOrHashtag.as_view(), name='add')
]