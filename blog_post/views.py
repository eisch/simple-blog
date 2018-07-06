from django.shortcuts import render
from django.http import HttpResponse
from blog_post.models import BlogPost


def show_all_blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'list_posts.html', {
        'posts': posts,
    }, content_type='text/html')
