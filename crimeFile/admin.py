from django.contrib import admin
from . import models

@admin.register(models.Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ['title', 'victim', 'status', 'type']