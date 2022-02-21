from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Complain

def FileHistoryView(request):
    if request.user.is_authenticated:
        complain_list_on_pending = Complain.objects.filter(user=request.user, status='pending')
        complain_list_on_investigation = Complain.objects.filter(user=request.user, status='investigating')
        complain_list_on_dismissed = Complain.objects.filter(user=request.user, status='dismissed')
        context = {
            'pending_complain_list': complain_list_on_pending,
            'investigating_complain_list': complain_list_on_investigation,
            'dismissed_complain_list': complain_list_on_dismissed,
        }
        return render(request, "file-history.html", context)
    return redirect('/login')

def addFileView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            title = request.POST['title']
            victim = request.POST['victim']
            suspect = request.POST['suspect']
            description = request.POST['description']
            phone = request.POST['phone']
            type = request.POST['type']
            todo = Complain.objects.create(title=title, user=user, criminal=suspect,victim=victim,phone=phone, description=description,type=type)
            todo.save()
            return redirect('fileHistoryView')

           
        else:
            return render(request, 'add-file.html')
    return redirect('/login')


