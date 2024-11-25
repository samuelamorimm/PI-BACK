from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from .models import Cliente

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

            if len(senha) < 8:
                messages.error(request, 'Sua senha tem que conter no minímo 8 caracteres')
                return redirect('login')


            if senha != confirmar_senha:
                messages.error(request, 'As senhas inseridas se diferem')
                return redirect('login')
            
            
            user = User.objects.filter(username=username)
            if user.exists():
                messages.error(request, 'Já existe alguém cadastrado com esse usuário')
                return redirect('login')
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha,
            )
            
            messages.success(request,'Usuário cadastrado com sucesso!')
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
                return redirect('login')
            
def logout(request):
    logout_django(request)
    return redirect('login')


@login_required
def editar_cliente(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        cliente = None

    if request.method == 'POST':
        if cliente:
            form = ClienteForm(request.POST, instance=cliente)
        else:
            form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            return redirect('cliente')
    else:
        if cliente:
            form = ClienteForm(instance=cliente)
        else:
            form = ClienteForm()

    return render(request, 'login/editar_cliente.html', {"form":form})


@login_required
def cliente(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        cliente = None

    return render(request, 'login/cliente.html', {"cliente": cliente})
