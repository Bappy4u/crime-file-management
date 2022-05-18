from django.db import models
from django.conf import settings


class Announcement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    noticeId = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='announcement', null=True)
    description = models.TextField()
    authority = models.CharField(max_length=255)
# Create your models here.
