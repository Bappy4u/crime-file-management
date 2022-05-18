from django.contrib import admin
from . import models

@admin.register(models.wantedPerson)
class WantedPersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.wantedPerson._meta.get_fields()]