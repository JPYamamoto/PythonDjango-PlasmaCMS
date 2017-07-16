from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from categories.models import Category

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_datetime = models.DateTimeField(default=timezone.now)
    last_update_datetime = models.DateTimeField()
    allow_comments = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='post/cover')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
