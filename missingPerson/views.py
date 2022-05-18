from django.shortcuts import render, redirect
from .models import MissingPerson

def missingPerson(request):
    missingPersons = MissingPerson.objects.all()
    context = {
        "missingPersons": missingPersons,
    }
    
    return render(request, 'missing-person.html', context)


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
