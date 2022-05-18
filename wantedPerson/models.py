from django.db import models
from django.conf import settings

# Create your models here.
class wantedPerson(models.Model):
    STATUS_ARRESTED = "ARRESTED"
    STATUS_WANTED = "WANTED"
   
    STATUS_CHOICES = [
        (STATUS_ARRESTED, 'Arrested'),
        (STATUS_WANTED, 'Wanted')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=STATUS_WANTED)
    photo = models.ImageField(upload_to='wanted-person', null=True)
    nid_birthid = models.CharField(max_length=255)
