from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):

  categories_data = [
    {
      'name': 'general',
      'tags': ['atkinsdiet', 'fatadapted', 'guthealth']
    },

    {
      'name': 'keto_foods',
      'tags': ['brain_foods', 'eatfat', 'paleo']
    },

    {
      'name': 'biohacking',
      'tags': ['bebetter', 'biohacking', 'wellness']
    }
  ]

  data = json.dumps(categories_data)

  return HttpResponse(data, content_type='application/json')

