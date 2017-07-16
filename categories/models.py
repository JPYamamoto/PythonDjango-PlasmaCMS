from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.ImageField(upload_to='category/icons')
    cover = models.ImageField(upload_to='category/covers')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
