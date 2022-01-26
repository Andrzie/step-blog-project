from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger


def posts(request):
    elems = Post.objects.all()
    paginator = Paginator(elems, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)

    return render(request, 'snblog/posts.html', {'elems': elems, 'page': page})

def post(request, pk):
    elem = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'snblog/post.html', {'elem': elem, 'comments': comments, 'form': form})

