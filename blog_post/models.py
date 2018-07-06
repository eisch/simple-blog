from django.db import models


class Tag(models.Model):
    name_tag = models.CharField(max_length=30)

    def __str__(self):
        return self.name_tag


class BlogPost(models.Model):
    title = models.TextField(unique=True)
    date_created = models.DateField()
    date_update = models.DateField()
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_email = models.EmailField()
    date_created = models.DateField()
    content = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
