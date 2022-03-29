from django.shortcuts import render

def missingPerson(request):
    return render(request, 'missing-person.html')
