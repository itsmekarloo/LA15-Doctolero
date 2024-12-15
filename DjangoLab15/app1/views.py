from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'app1/blog_list.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'app1/blog_detail.html', {'post': post})
