from django.urls import path
from .import views

app_name = 'child_001'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.readmore, name='readmore'),
    path('blog/cat/<int:id>/', views.cat, name='cat')
]