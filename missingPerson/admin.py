from django.contrib import admin
from . import models

@admin.register(models.MissingPerson)
class MissingPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'birthDate', 'user']