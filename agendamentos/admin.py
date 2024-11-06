from django.contrib import admin
from .models import Agendamento, Medico, Servico, ServicosAgendamentos, Horario

# Register your models here.
admin.site.register(Agendamento)
admin.site.register(Medico)
admin.site.register(Servico)
admin.site.register(ServicosAgendamentos)
admin.site.register(Horario)