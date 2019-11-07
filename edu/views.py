from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context

from . import models
from django.views import generic


def index(request):
    return render(request, 'edu/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        context = {"mode": 0}
        flag = False
        if User.objects.filter(username=username).exists():
            flag = True
        if password2 != password and flag:
            context = {"mode": 3}
        if password2 == password and flag:
            context = {"mode": 2}
        if password2 != password and not flag:
            context = {"mode": 1}
        if password2 == password and not flag:
            user = models.User.objects.create_user(first_name=first_name, last_name=last_name,
                                                   email=email, username=username, password=password)
            user.save()
        return render(request, 'edu/formValidator.html', context)
    else:
        return render(request, 'edu/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'edu/loggedIn.html')
        else:
            return render(request, 'edu/loggedFailed.html')
    return render(request, 'edu/login.html')
