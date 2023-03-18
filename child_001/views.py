from django.shortcuts import render, HttpResponse
from . models import Blog, Category, Logo
# Create your views here.

# def home(request):
#     return render(request, 'blog/index.html')

def home(request):
    return render(request, 'blog/home-main.html')

def blog(request):
    data = Blog.objects.all().order_by('-id')
    logo = Logo.objects.all()
    context = {'dt': data, 'logo': logo}
    return render(request, 'blog/blog.html', context)

def readmore(request, id):
    data = Blog.objects.get(pk=id)
    logo = Logo.objects.all()
    print(data)
    context = {'rd': data, 'logo': logo}
    return render(request, 'blog/blog-read-more.html', context)   

def cat(request, id):
    data = Blog.objects.filter(category_name_id=id).order_by('-id')
    data2 = Blog.objects.all()
    logo = Logo.objects.all()
    print(data2)
    context = {'rd': data, 'dta': data2, 'logo': logo}
    return render(request, 'blog/categoryDetail.html', context)  
