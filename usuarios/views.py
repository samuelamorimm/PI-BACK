from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Usuário existente')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Cadastrado com sucesso')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('agendamentos')
        else:
            return render(request, 'login.html')