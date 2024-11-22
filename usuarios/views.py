from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'login.html',)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirmar_senha = request.POST.get('confirmar_senha')

            if senha != confirmar_senha:
                messages.error(request, 'As senhas inseridas se diferem')
                return redirect('login')
            
            if len(senha) < 8:
                messages.error(request, 'Sua senha tem que conter no minímo 8 caracteres')
                return redirect('login')
            
            user = User.objects.filter(email=email)
            if user.exists():
                messages.error(request, 'Já existe um usuário cadastrado com esse E-mail')
                return redirect('login')
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha,
            )
            
            return redirect('login')


        

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['senha']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login_django(request, user)
                return redirect('agendamentos')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')
                return redirect(login)
            
def logout(request):
    logout_django(request)
    return redirect('login')