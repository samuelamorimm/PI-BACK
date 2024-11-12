from django.shortcuts import render, redirect, get_object_or_404

from agendamentos.models import Agendamento,Medico, ServicosAgendamentos
from .forms import AgendamentoForm,MedicoForm, AgendaForm

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
def medicos(request):
    form = MedicoForm
    medicos = Medico.objects.all()
    return render(request, 'medico.html', {'form':form, 'medicos':medicos})

def add_medico(request):
    if request.method == 'POST':
        print(request.POST)
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(medicos)
    else:
        form = AgendamentoForm()
    return redirect(medicos)

def medico_delete(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect(medicos)

#medicos --------------------

#agendas -----------------------
def agendas(request):
    agendas = ServicosAgendamentos.objects.all()
    form = AgendaForm()
    return render(request, 'agenda.html', {'agendas':agendas, 'form': form})

def add_agenda(request):
    if request.method == 'POST':
        print(request.POST)
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(agendas)
    else:
        form = AgendamentoForm()
    return redirect(agendas)
#agendas -----------------------

