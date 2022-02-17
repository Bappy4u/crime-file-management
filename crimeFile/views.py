from django.http import HttpResponse
from django.shortcuts import redirect, render

def FileHistoryView(request):
    if request.user.is_authenticated:
        return render(request, "file-history.html")
    return redirect('/login')

