from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from django.views import generic


def index(request):
    return render(request, 'edu/index.html')


def register(request):
    return render(request, 'edu/register.html')


def addUser(request):
    user = models.User.objects.create()
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.password = request.POST['password1']
        user.save()
        return redirect('/')


def login(request):
    return render(request, 'edu/login.html')


def loginRequest(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'edu/loggedIn')
    else:
        return render(request, 'edu/Error.html')

