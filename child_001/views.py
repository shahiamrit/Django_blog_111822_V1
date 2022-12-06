from django.shortcuts import render
from . models import Blog
# Create your views here.

def home(request):
    return render(request, 'blog/index.html')


def blog(request):
    data = Blog.objects.all()
    context = {'dt': data}
    return render(request, 'blog/blog.html', context)

def readmore(request, id):
    data = Blog.objects.get(pk=id)
    print(data)
    context = {'rd': data}
    return render(request, 'blog/blog-read-more.html', context)    