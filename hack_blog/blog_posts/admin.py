from django.contrib import admin
from .models import BlogPost, Comment, Tag


admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(Comment)
