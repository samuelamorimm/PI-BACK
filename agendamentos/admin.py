from django.contrib import admin
from .models import Agendamento, Medico, Servico, ServicosAgendamentos

# Register your models here.
admin.site.register(Agendamento)
admin.site.register(Medico)
admin.site.register(Servico)
admin.site.register(ServicosAgendamentos)