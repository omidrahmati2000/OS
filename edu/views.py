from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

from . import models

log = False


def index(request):
    global log
    return render(request, 'edu/index.html', {'log': log})


def register(request):
    global log
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        e = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']
        context = {"mode": 0, 'log': log}
        flag = False
        if User.objects.filter(username=username).exists():
            flag = True
        if password2 != password and flag:
            context = {"mode": 3, 'log': log}
        if password2 == password and flag:
            context = {"mode": 2, 'log': log}
        if password2 != password and not flag:
            context = {"mode": 1, 'log': log}
        if password2 == password and not flag:
            user = models.User.objects.create_user(first_name=first_name, last_name=last_name,
                                                   email=e, username=username, password=password)
            user.save()
        return render(request, 'edu/formValidator.html', context)
    else:
        return render(request, 'edu/register.html', {'log': log})


def login_view(request):
    global log
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log = True
            login(request, user)
            return render(request, 'edu/loggedIn.html', {'log': log})
        else:
            return render(request, 'edu/loggedFailed.html', {'log': log})
    return render(request, 'edu/login.html', {'log': log})


def contactUs(request):
    global log
    if request.method == 'POST':
        subject = request.POST['title']
        message = request.POST['text']
        e = request.POST['email']
        message += e
        email(request, subject, message)
        return render(request, 'edu/contactSubmitted.html', {'log': log})
    else:
        return render(request, 'edu/contactUs.html', {'log': log})


def logout_view(request):
    global log
    log = False
    logout(request)
    return redirect('/')


def email(request, subject, message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['webe19lopers@gmail.com']
    send_mail(subject, message, email_from, recipient_list)


@login_required
def profile(request):
    global log
    first_name = request.user.first_name
    last_name = request.user.last_name
    username = request.user.username
    print(username)
    return render(request, 'edu/profile.html', {'log': log, 'first': first_name, 'last': last_name, 'username': username})


@login_required
def setting(request):
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        if first:
            request.user.first_name = first
            request.user.save()
        if first:
            request.user.last_name = last
            request.user.save()
        return render(request, 'edu/setting.html', {'log': log})
    else:
        return render(request, 'edu/setting.html', {'log': log})


@login_required
def course(request):
    if request.method == 'POST':
        department = request.POST['department']
        name = request.POST['name']
        course_number = request.POST['course_number']
        group_number = request.POST['group_number']
        teacher = request.POST['teacher']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        first_day = request.POST['first_day']
        second_day = request.POST['second_day']
        new_course = models.Course(department=department,name=name,course_number=course_number
                                                  ,group_number=group_number,teacher=teacher,start_time=start_time
                                                  ,end_time=end_time,first_day=first_day,second_day=second_day)
        new_course.save()
        return render(request, 'edu/createCourse.html', {'log': log})
    else:
        return render(request, 'edu/createCourse.html', {'log': log})


@login_required
def showCourses(request):
    data = models.Course.objects.all()
    stu = {
        'log': log,
        "courses": data
    }
    return render(request, 'edu/showCourses.html', stu)
