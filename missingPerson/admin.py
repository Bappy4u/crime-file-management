from django.contrib import admin
from . import models

@admin.register(models.MissingPerson)
class MissingPersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.MissingPerson._meta.get_fields()]