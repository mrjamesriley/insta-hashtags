from django.shortcuts import render

def home(request):
    return render(request, 'generator/home.html')

def add(request):
    return render(request, 'generator/add.html')