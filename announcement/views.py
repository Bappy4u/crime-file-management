from django.shortcuts import render
from .models import Announcement

# Create your views here.

def announcementView(request):
    announcements = Announcement.objects.all()
    context = { 
        'announcements': announcements
    }
       
    return render(request, 'announcement.html', context)
