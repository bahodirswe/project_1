from django.contrib import admin
from blog.models import Category, Post


admin.site.register([Category, Post])
