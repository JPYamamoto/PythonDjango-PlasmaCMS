from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    job = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='profile/images', null=True)
    bio = models.TextField(blank=True, null=True)
    sn_facebook = models.URLField(blank=True, null=True)
    sn_twitter = models.URLField(blank=True, null=True)
    sn_medium = models.URLField(blank=True, null=True)
    sn_github = models.URLField(blank=True, null=True)
    sn_linkedin = models.URLField(blank=True, null=True)
    sn_youtube = models.URLField(blank=True, null=True)
    sn_google = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
