from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    re_path(r'^profile/?$', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit'),
    path('login', login, name='login'),
    path('logout', logout, {'next_page':'login'}, name='logout'),
    path('test', views.test, name='test'),


]