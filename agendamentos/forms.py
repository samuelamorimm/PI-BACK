from django import forms
from .models import Agendamento, Especialidade, Medico, ServicosAgendamentos

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'

    

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class AgendaForm(forms.ModelForm):
    class Meta:
        model = ServicosAgendamentos
        fields = '__all__'
        
class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = '__all__'

