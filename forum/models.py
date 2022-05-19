from unicodedata import category
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='forum')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

