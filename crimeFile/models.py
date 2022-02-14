from django.db import models
from django.conf import settings


class Complain(models.Model):
    COMPLAIN_TYPE_GD = 'GD'
    COMPLAIN_TYPE_CASE_FILE = 'CF'
    COMPLAIN_TYPE_CHOICES = [
        (COMPLAIN_TYPE_GD, 'GD'),
        (COMPLAIN_TYPE_CASE_FILE, 'CASE FILE'),
        
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    criminal = models.CharField(max_length=1000)
    victim = models.CharField(max_length=255)
    type = models.CharField(
        max_length=2, choices=COMPLAIN_TYPE_CHOICES, default=COMPLAIN_TYPE_GD)
    phone = models.CharField(max_length=255)
    # file = models.ImageField()