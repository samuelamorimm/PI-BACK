from django.shortcuts import render

from agendamentos.models import Agendamento

# Create your views here.
def agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'index.html', {'agendamentos': agendamentos})