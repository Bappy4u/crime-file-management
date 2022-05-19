from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    nid = models.CharField(unique=True, max_length=20)
    photo = models.ImageField(upload_to = 'profile-photo', null='True')

# Create your models here.
