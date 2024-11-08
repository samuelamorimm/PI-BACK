from django.shortcuts import render, redirect, get_object_or_404

from agendamentos.models import Agendamento
from .forms import AgendamentoForm

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

