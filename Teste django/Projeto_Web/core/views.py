from django.shortcuts import render
from django.http import request

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')