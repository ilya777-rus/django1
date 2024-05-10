from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from . import models


def index(request):
    posts = models.Post.objects.all()
    categories = models.Category.objects.all()
    context = {
               'posts': posts,
               'categories':categories,
               "title": "Список постов",
               }
    return render(request, 'core/index.html', context=context)
    # return HttpResponse(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

def get_category(request, category_id):
    posts = models.Post.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
               'posts': posts,
               'categories':categories,
               "category": category,
               }
    return render(request, 'core/category.html', context=context)
