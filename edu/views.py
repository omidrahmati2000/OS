from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from django.views import generic


def index(request):
    return render(request, 'edu/index.html')


def register(request):
    return render(request, 'edu/register.html')


def addUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = models.User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                                          password1=password1, password2=password2)
        user.save()
        return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+' '+password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('1')
            return render(request, 'edu/loggedIn.html')
        else:
            print('2')
            return render(request, 'edu/loggedFailed.html')
    print('GET')
    return render(request, 'edu/login.html')
