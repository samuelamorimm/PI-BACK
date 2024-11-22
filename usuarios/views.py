from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from .forms import UserForm

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'login.html',)
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                f = form.save()
                f.set_password(f.password)
                f.save()
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect(login)


        

def login(request):
    if request.method == 'GET':
        form = UserForm(request.POST)
        return render(request, 'login.html',  {"form":form})
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_django(request, user)
                return redirect('agendamentos')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')
                return redirect(login)