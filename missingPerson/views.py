from django.http import Http404
from django.shortcuts import render, redirect
from .models import MissingPerson

def missingPerson(request):
    missingPersons = MissingPerson.objects.all().filter(status="MISSING")
    context = {
        "missingPersons": missingPersons,
    }
    
    return render(request, 'missing-person.html', context)




def pendingMissingPerson(request):
    missingPersons = MissingPerson.objects.all().filter(status="PENDING")
    context = {
        "missingPersons": missingPersons,
    }
    
    return render(request, 'pending-missing-person.html', context)


def addMissingPerson(request):
    if request.method == 'POST':
           
            user = request.user
            name = request.POST['name']
            street = request.POST['street']
            village = request.POST['village']
            city = request.POST['city']
            description = request.POST['description']
            phone = request.POST['phone']
            photo = request.FILES.get('photo')
            date = request.POST['date']
            bdate = request.POST['bdate']
            person = MissingPerson.objects.create(name=name, birthDate=bdate, user=user, street=street,village=village,contact=phone, city=city, date = date, description=description, photo = photo)
            person.save()
            return redirect('missingPerson')
    return render(request, 'add-missing-person.html')



def missingPersonDet(request, id):
    try:
        person = MissingPerson.objects.get(pk=id)
    except MissingPerson.DoesNotExist:
        raise Http404("File does not exist")
        
    context = {
        'person': person
    }
    return render(request, 'missing-person-det.html', context)
