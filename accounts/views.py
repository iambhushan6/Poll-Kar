from django.http.response import HttpResponse
from accounts.forms import CreateUserForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.


def loginkar(request):
    if request.user.is_authenticated:
        return redirect('allpolls')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('allpolls')
        else: HttpResponse('Invalid Credentials!')

    return render(request, 'accounts/login.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('allpolls')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = CreateUserForm()
    return render(request, 'accounts/signup.html', {'form':form})

def logoutkar(request):
    logout(request)
    return redirect('login')
