from django.db import models
import os

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=150)
    slogan = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='blog/icons')
    cover = models.ImageField(upload_to='blog/cover')
    sn_facebook = models.URLField(blank=True)
    sn_twitter = models.URLField(blank=True)
    sn_medium = models.URLField(blank=True)
    sn_github = models.URLField(blank=True)
    sn_linkedin = models.URLField(blank=True)
    sn_youtube = models.URLField(blank=True)
    sn_google = models.URLField(blank=True)
