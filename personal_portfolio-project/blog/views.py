from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    # The following shows the 5 most recent blogs
    #blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs })
