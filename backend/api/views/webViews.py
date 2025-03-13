from django.shortcuts import render
from api.models import *

def home(request):
    user = CustomUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})

def criarAluno(request):
    return render(request, 'criarAluno.html')

def login(request):
    return render(request,'login.html')