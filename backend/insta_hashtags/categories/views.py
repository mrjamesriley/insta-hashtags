from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
import json


def index(request):
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

