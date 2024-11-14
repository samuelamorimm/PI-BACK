from django.contrib import admin
from .models import Agendamento, Medico, Especialidade, ServicosAgendamentos

# Register your models here.
admin.site.register(Agendamento)
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(ServicosAgendamentos)