from django.shortcuts import render
from django.http import request

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def esqueci(request):
    return render(request, 'esqueci.html')

def criar(request):
    return render(request, 'criar.html')

