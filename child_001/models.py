from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Category Name")
    def __str__(self):
        return self.name

class Blog(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.category_name.name
class test(models.Model):
    name = models.TextField()

# Logo
class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')
    
