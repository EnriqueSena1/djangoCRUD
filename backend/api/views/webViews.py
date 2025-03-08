from django.shortcuts import render
from api.models import *

def home(request):
    # alunos = Aluno.objects.all()
    # return render(request, 'home.html', {'alunos': alunos})
    pass

def criarAluno(request):
    return render(request, 'criarAluno.html')

def login(request):
    return render(request,'login.html')