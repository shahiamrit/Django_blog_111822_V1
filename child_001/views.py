from django.shortcuts import render, HttpResponse
from . models import Blog, Category
# Create your views here.

# def home(request):
#     return render(request, 'blog/index.html')

def home(request):
    return render(request, 'blog/home-main.html')

def blog(request):
    data = Blog.objects.all()
    context = {'dt': data}
    return render(request, 'blog/blog.html', context)

def readmore(request, id):
    data = Blog.objects.get(pk=id)
    print(data)
    context = {'rd': data}
    return render(request, 'blog/blog-read-more.html', context)   

def cat(request, id):
    data = Blog.objects.filter(category_name_id=id)
    data2 = Blog.objects.all()
    print(data2)
    context = {'rd': data, 'dta': data2}
    return render(request, 'blog/categoryDetail.html', context)  