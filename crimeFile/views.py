from django.http import HttpResponse
from django.shortcuts import render

def loginView(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>You are already logged in</h1>")
    return render(request, "index.html")
