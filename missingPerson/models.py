from contextlib import nullcontext
from django.db import models
from django.conf import settings


class MissingPerson(models.Model):
    STATUS_FOUND = "FOUND"
    STATUS_MISSING = "MISSING"
    STATUS_PENDING = "PENDING"
    STATUS_CHOICES = [
        (STATUS_FOUND, 'Found'),
        (STATUS_MISSING, 'Missing'),
        (STATUS_PENDING, 'Pending')
    ]
        

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='missing-person', null=True)
    description = models.CharField(max_length=500 , null=True)
    street = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=False)
    date = models.DateTimeField()
    birthDate = models.DateField(null=True)
    contact = models.CharField(max_length=255, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=7, default=STATUS_PENDING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
