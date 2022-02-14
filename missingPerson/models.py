from django.db import models
from django.conf import settings


class MissingPerson(models.Model):
    name = models.CharField(max_length=255)
    # photo = models.ImageField()
    street = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=False)
    date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
