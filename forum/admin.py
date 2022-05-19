from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Post._meta.get_fields()]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Category._meta.get_fields()]