from django.contrib import admin
from . import models

@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = list_display = [field.name for field in models.Announcement._meta.get_fields()]