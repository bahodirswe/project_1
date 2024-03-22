from django.shortcuts import render
from blog.models import Post, Category

def home(request):
    posts = Post.objects.all()

    data = {
        "posts": posts
    }
    return render(request, "home.html", data)