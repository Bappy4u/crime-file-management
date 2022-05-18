from django.shortcuts import render
from .models import wantedPerson

def wantedPersonView(request):
    wantedPersons = wantedPerson.objects.all()
    context = {
        "wantedPersons": wantedPersons,
    }
    return render(request, 'wanted-person.html', context)

