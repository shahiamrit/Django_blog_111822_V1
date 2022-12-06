from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Blog, Category
# Register your models here.

admin.site.register(Category)
class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Blog, BlogModelAdmin)