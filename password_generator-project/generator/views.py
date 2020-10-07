import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': ''})

def password(request):
    # Default: lowercase letters
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # Uppercase letters
    if request.GET.get('uppercase'):characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Special characters
    if request.GET.get('special'):characters.extend('!@#$%^&*()')
    # Numbers
    if request.GET.get('numbers'):characters.extend('0123456789')
    # Default length is 12
    length = int(request.GET.get('length',25))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
