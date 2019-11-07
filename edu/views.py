from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, 'edu/index.html')
