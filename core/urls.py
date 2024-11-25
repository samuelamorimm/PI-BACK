from django.contrib import admin
from django.urls import include, path
from agendamentos.views import agendamentos, agendar, deletar_agendamento, medico_view, medico_create, medico_delete, agenda_view, agenda_create, agenda_delete, especialidade_view, especialidade_create, especialidade_delete

from usuarios import views as views_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', agendamentos, name='agendamentos'),
    path('agendar/', agendar, name='agendar'),
    path('deletar/<int:id>', deletar_agendamento, name='deletar_agendamento'),
    path('medico/', medico_view, name='medicos_view'),
    path('medicoadd/', medico_create, name='medico_create'),
    path('medicodel/<int:id>', medico_delete, name='medico_delete'),
    path('agenda/', agenda_view, name='agendas_view'),
    path('addagenda/', agenda_create, name='add_agenda'),
    path('delagenda/<int:id>', agenda_delete, name='agenda_delete'),
    path('especialidades', especialidade_view, name='especialidades_view'),
    path('especialidadeadd/', especialidade_create, name='especialidade_create'),
    path('especialidadedel/<int:id>', especialidade_delete, name ='especialidade_delete'),


    path('accounts/', include('usuarios.urls')),


    path('cliente', views_usuarios.cliente, name='cliente'),
    path('editar_cliente', views_usuarios.editar_cliente, name='editar_cliente'),

 # URLs do django-allauth
    path('accounts/', include('allauth.urls')), 
]
