from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from agendamentos.models import Agendamento,Medico, ServicosAgendamentos, Especialidade
from .forms import AgendamentoForm,MedicoForm, AgendaForm, EspecialidadeForm

# Create your views here.

@login_required
def agendamentos(request):
    form = AgendamentoForm()
    agendamentos = Agendamento.objects.all()
    return render(request, 'clinica/index.html', {'agendamentos': agendamentos, 'form':form})

@login_required
def agendar(request):
    if request.method == 'POST':
        print(request.POST)

        data = request.POST.get('data')
        servico_id = request.POST.get('servico')
        servico = ServicosAgendamentos.objects.filter(id=servico_id).first()
        
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.user = request.user
            agendamento.data = data
            agendamento.servico = servico
            agendamento.save()
    else:
        form = AgendamentoForm()
    return redirect(agendamentos)

@login_required
def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.status = 'F'

    context = {
        "agendamento" : agendamento
    }

    return render(request, 'clinica/agendamento.html', context)

@login_required
def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect(agendamentos)

@login_required
def alterar_status_f(request, id): #finalizar agendamento
    a = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        a.status = 'F'
        a.save()
        return redirect('home')
    
    return redirect('home')

@login_required
def alterar_status_i(request, id): #iniciar agendamento
    a = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        print("certyofkdjgsljgjsdjglkjdsfg")
        a.status = 'A'
        a.save()
        return redirect('home')
    
    return redirect('home')

def buscar_servicos(request, data):
    try:
         # Convertendo a string da data para o formato de data que o Django entende
        data = datetime.strptime(data, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({"error": "Data inválida"}, status=400)

    servicos = ServicosAgendamentos.objects.filter(data=data).distinct()

    servicos_data = [{"id": servico.id, "servico": str(servico)} for servico in servicos]
    
    return JsonResponse({"servicos": servicos_data})

#medicos --------------------
@login_required
def medico_view(request):
    if not request.user.is_staff: #se usuário não for adm
        return redirect('home')

    form = MedicoForm
    medicos = Medico.objects.all()
    return render(request, 'clinica/medico.html', {'form':form, 'medicos':medicos})

def medico_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(medico_view)
    else:
        form = AgendamentoForm()
    return redirect(medico_view)

def medico_delete(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect(medico_view)

#medicos --------------------

#agendas -----------------------
@login_required
def agenda_view(request):
    if not request.user.is_staff: #se usuário não for adm
        return redirect('home')

    agendas = ServicosAgendamentos.objects.all()
    form = AgendaForm()
    return render(request, 'clinica/agenda.html', {'agendas':agendas, 'form': form})

def agenda_create(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit=False)
            agenda.data = data
            agenda.save()
            return redirect(agenda_view)
    else:
        form = AgendamentoForm()
        print('falhou')
    return redirect(agenda_view)

def agenda_delete(request, id):
    agenda = get_object_or_404(ServicosAgendamentos, id=id)
    agenda.delete()
    return redirect(agenda_view)
#agendas -----------------------

#especialidades -----------------------------------------
@login_required
def especialidade_view(request):
    especialidades = Especialidade.objects.all()
    form = EspecialidadeForm
    return render(request, 'clinica/especialidade.html', {'especialidades':especialidades, 'form':form})

def especialidade_create(request):
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(especialidade_view)
    else:
        form = EspecialidadeForm
    return redirect(especialidade_view)

def especialidade_delete(request, id):
    especialidade = get_object_or_404(Especialidade, id=id)
    especialidade.delete()
    return redirect(especialidade_view)
#especialidades -----------------------------------------

