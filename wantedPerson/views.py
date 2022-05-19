from django.http import Http404
from django.shortcuts import render
from .models import wantedPerson

def wantedPersonView(request):
    wantedPersons = wantedPerson.objects.all()
    context = {
        "wantedPersons": wantedPersons,
    }
    return render(request, 'wanted-person.html', context)


def personDetView(request, id):
    try:
        person = wantedPerson.objects.get(pk=id)
    except wantedPerson.DoesNotExist:
        raise Http404("File does not exist")
        
    context = {
        'person': person
    }
    return render(request, 'wanted-person-det.html', context)