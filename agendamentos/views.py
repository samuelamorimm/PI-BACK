from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from agendamentos.models import Agendamento,Medico, ServicosAgendamentos, Especialidade
from .forms import AgendamentoForm,MedicoForm, AgendaForm, EspecialidadeForm

# Create your views here.

@login_required
def agendamentos(request):
    form = AgendamentoForm()
    if request.user.is_staff:  # Se for admin, ele verá todos os agendamentos
        agendamentos = Agendamento.objects.all()
    else:
        # Caso contrário, só mostra os agendamentos do próprio usuário
        agendamentos = Agendamento.objects.filter(user=request.user)
    return render(request, 'clinica/index.html', {'agendamentos': agendamentos, 'form':form})

def agendar(request):
    if request.method == 'POST':
        print(request.POST)

        data = request.POST.get('data')
        
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.user = request.user
            agendamento.data = data
            agendamento.save()
    else:
        form = AgendamentoForm()
    return redirect(agendamentos)


def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect(agendamentos)

#medicos --------------------
@login_required
def medico_view(request):
    if not request.user.is_staff: #se usuário não for adm
        return redirect('agendamentos')

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
        return redirect('agendamentos')

    agendas = ServicosAgendamentos.objects.all()
    form = AgendaForm()
    return render(request, 'clinica/agenda.html', {'agendas':agendas, 'form': form})

def agenda_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
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

