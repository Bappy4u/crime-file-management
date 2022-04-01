from django.db import models
from django.conf import settings


class MissingPerson(models.Model):
    STATUS_FOUND = "FOUND"
    STATUS_MISSING = "MISSING"
    STATUS_CHOICES = [
        (STATUS_FOUND, 'Found'),
        (STATUS_MISSING, 'Missing'),
    ]
        

    name = models.CharField(max_length=255)
    # photo = models.ImageField()
    street = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=False)
    date = models.DateTimeField()
    birthDate = models.DateField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=7, default=STATUS_MISSING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
