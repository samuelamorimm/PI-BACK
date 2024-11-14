from django.shortcuts import render, redirect, get_object_or_404

from agendamentos.models import Agendamento,Medico, ServicosAgendamentos, Especialidade
from .forms import AgendamentoForm,MedicoForm, AgendaForm, EspecialidadeForm

# Create your views here.


def agendamentos(request):
    form = AgendamentoForm()
    agendamentos = Agendamento.objects.all()
    return render(request, 'index.html', {'agendamentos': agendamentos, 'form':form})

def agendar(request):
    if request.method == 'POST':
        print(request.POST)
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(agendamentos)
    else:
        form = AgendamentoForm()
    return redirect(agendamentos)

def deletar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    agendamento.delete()
    return redirect(agendamentos)

#medicos --------------------
def medico_view(request):
    form = MedicoForm
    medicos = Medico.objects.all()
    return render(request, 'medico.html', {'form':form, 'medicos':medicos})

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
def agenda_view(request):
    agendas = ServicosAgendamentos.objects.all()
    form = AgendaForm()
    return render(request, 'agenda.html', {'agendas':agendas, 'form': form})

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
def especialidade_view(request):
    especialidades = Especialidade.objects.all()
    form = EspecialidadeForm
    return render(request, 'especialidade.html', {'especialidades':especialidades, 'form':form})

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

