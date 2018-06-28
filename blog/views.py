from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all().first()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    print(slug)
    posts = Post.objects.all()
    # post.html here is the template you want use
    return render_to_response('post.html', {'post': get_object_or_404(Post, slug=slug), 'posts': posts})


def about(request):
    return render(request, 'about.html', {})