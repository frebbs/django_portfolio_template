from django.shortcuts import render
from .models import Blog
# Create your views here.


def all_blogs(req):
    blogs = Blog.objects.order_by('-date')[:3]
    return render(req, 'blog/all_blogs.html', {
        'blog': blogs
    })