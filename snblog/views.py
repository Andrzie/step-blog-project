from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    elems = Post.objects.all()
    return render(request, 'snblog/posts.html', {'elems': elems})

def post(request, pk):
    elem = get_object_or_404(Post, pk=pk)
    return render(request, 'snblog/post.html', {'elem': elem})

