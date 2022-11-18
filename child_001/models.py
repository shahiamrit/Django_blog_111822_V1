from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    body = models.TextField()
    def __str__(self):
        return self.name

    