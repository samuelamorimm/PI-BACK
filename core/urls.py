from django.contrib import admin
from django.urls import include, path
from agendamentos.views import agendamentos, agendar, deletar_agendamento, editar_agendamento, medico_view, medico_create, medico_delete, agenda_view, agenda_create, agenda_delete, especialidade_view, especialidade_create, especialidade_delete, alterar_status_f, alterar_status_i, buscar_servicos

from usuarios import views as views_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', agendamentos, name='home'),
    path('agendar/', agendar, name='agendar'),
    path('editar-agendamento/<int:id>', editar_agendamento, name='editar_agendamento'),
    path('deletar-agendamento/<int:id>', deletar_agendamento, name='deletar_agendamento'),
    path('alterar-status/<int:id>/finalizar', alterar_status_f, name='alterar_status_finalizar'),
    path('alterar-status/<int:id>/iniciar', alterar_status_i, name='alterar_status_iniciar'),
    path('buscar-servicos/<str:data>/', buscar_servicos, name='buscar_servicos'),


    path('medico/', medico_view, name='medicos_view'),
    path('adicionar-medico/', medico_create, name='medico_create'),
    path('deletar-medico/<int:id>', medico_delete, name='medico_delete'),


    path('agenda/', agenda_view, name='agendas_view'),
    path('addagenda/', agenda_create, name='add_agenda'),
    path('delagenda/<int:id>', agenda_delete, name='agenda_delete'),


    path('especialidades/', especialidade_view, name='especialidades_view'),
    path('especialidadeadd/', especialidade_create, name='especialidade_create'),
    path('especialidadedel/<int:id>', especialidade_delete, name ='especialidade_delete'),


    path('accounts/', include('usuarios.urls')),


    path('cliente/', views_usuarios.cliente, name='cliente'),
    path('editar_cliente/', views_usuarios.editar_cliente, name='editar_cliente'),

 # URLs do django-allauth
    #path('accounts/', include('allauth.urls')), 
]
