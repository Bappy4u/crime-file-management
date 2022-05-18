from django.shortcuts import render
from .models import MissingPerson

def missingPerson(request):
    missingPersons = MissingPerson.objects.all()
    context = {
        "missingPersons": missingPersons,
    }
    
    return render(request, 'missing-person.html', context)


def addMissingPerson(request):
    return render(request, 'add-missing-person.html')
