from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# FIXME: have it so that our frontend supports CSRF, rather than disabling
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def index(request):
  if request.method == "GET":
    return get_categories(request)
  elif request.method == "POST":
    return add_category(request)

def get_categories(request):
  all_categories = Category.objects.filter(user_id= request.user.id)
  catergories_response = []

  for category in all_categories:
    hashtags_list = []
    all_hashtags = category.hashtag_set.all()

    for hashtag in all_hashtags:
      hashtags_list.append({
        'name':hashtag.hashtag,
        'id': hashtag.id,
      })

    category_dict = {
      'name': category.category_name,
      'id': category.category_id,
      'hashtags': hashtags_list
    }
    catergories_response.append(category_dict)

  all_categories_json = json.dumps(catergories_response)
  return HttpResponse(all_categories_json)

def add_category(request):
  # 1. have it create a category for the user with the passed in name (unless it already exists)
  # 2. respond with the created category object as json
  # 3. have Vue on frontend, push the category onto its categories array
  #  Category.objects.create(category_name=request.name, user_id=request.user.id)
  response_data = json.dumps({ 'status': 'ok', 'pokemon': 'red' })
  return  HttpResponse(response_data)