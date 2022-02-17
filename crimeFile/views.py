from django.http import HttpResponse
from django.shortcuts import render

def loginView(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>You are already logged in</h1>")
    return render(request, "login.html")

def FileHistoryView(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>You are already logged in</h1>")
    return render(request, "file-history.html")

