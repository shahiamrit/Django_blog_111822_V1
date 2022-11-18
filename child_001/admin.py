from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Blog
# Register your models here.

class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Blog, BlogModelAdmin)