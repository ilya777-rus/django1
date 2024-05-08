from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from . import models


def index(request):
    posts = models.Post.objects.all()

    return render(request, 'core/index.html', context={'posts':posts, "title":"Список постов"})
    # return HttpResponse(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

