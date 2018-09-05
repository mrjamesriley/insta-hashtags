from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.create, name='create', method='post')
]
