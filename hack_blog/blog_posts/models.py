from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)


class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=255)
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    post_content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="tags")


class Comment(models.Model):
    email = models.EmailField()
    date_created = models.DateField()
    comment_content = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
