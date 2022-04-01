from django.shortcuts import render
from .models import MissingPerson

def missingPerson(request):
    missingPersons = MissingPerson.objects.all()
    context = {
        "missingPersons": missingPersons,
    }
    
    return render(request, 'missing-person.html', context)
