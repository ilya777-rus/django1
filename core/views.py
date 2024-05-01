from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

