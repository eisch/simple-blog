from django.contrib import admin
from blog_post.models import Tag, BlogPost, Comment
# Register your models here.


class AllAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, AllAdmin)
admin.site.register(BlogPost, AllAdmin)
admin.site.register(Comment, AllAdmin)
