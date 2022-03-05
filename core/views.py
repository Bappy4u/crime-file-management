from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/crime-file')
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/crime-file')
    
    return render(request, "login.html")

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('loginView')


def signupView(request):
    if request.user.is_authenticated:
        return redirect('/crime-file')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
    return render(request, 'signup.html')

