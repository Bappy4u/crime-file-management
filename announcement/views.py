from django.http import Http404
from django.shortcuts import render
from .models import Announcement

# Create your views here.

def announcementView(request):
    announcements = Announcement.objects.all()
    context = { 
        'announcements': announcements
    }
       
    return render(request, 'announcement.html', context)


def singleNoticeView(request, id):

    try:
        file = Announcement.objects.get(pk=id)
    except Announcement.DoesNotExist:
        raise Http404("File does not exist")
        
    context = {
        'file': file
    }
    return render(request, 'notice-det.html', context)