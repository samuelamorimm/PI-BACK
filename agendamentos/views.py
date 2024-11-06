from django.shortcuts import render

from agendamentos.models import Agendamento
from .forms import AgendamentoForm

# Create your views here.
def agendamentos(request):
    form = AgendamentoForm(request.POST)
    agendamentos = Agendamento.objects.all()
    return render(request, 'index.html', {'agendamentos': agendamentos, 'form':form})