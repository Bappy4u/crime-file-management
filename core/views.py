from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from .models import User


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/crime-file')
    if request.method == 'POST' and not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        nid = request.POST['nid']
        email = request.POST['email']
        context = {}
        got_error = False
        if User.objects.get(email=email):
            got_error = True
            context['email'] = "This email is already registered"

        if User.objects.get(nid=nid):
            got_error = True
            context['nid'] = 'This nid is already used by another user'
            
        if User.objects.get(username=username):
            got_error = True
            context['username']='Username already exist. it must be unique'

        if got_error:
            context['got_error'] = True
            return render(request, 'signup.html', context)
        user = User.objects.create_user(username=username,password=password,first_name=firstName,last_name=lastName,email=email,nid=nid)
        login(request, user)
        return redirect('fileHistoryView')
    return render(request, 'signup.html')

