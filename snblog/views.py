from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'snblog/index.html', {'posts': posts})

