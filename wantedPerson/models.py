from django.db import models

# Create your models here.
class wantedPerson(models.model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    #photo = models.imageField()
    nid_birthid = models.CharField(max_length=255)
