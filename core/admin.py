from django.contrib import admin
from . import models
# from .models import Category, Post

admin.site.register(models.Category)
admin.site.register(models.Post)
# Register your models here.
