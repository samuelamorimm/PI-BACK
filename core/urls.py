"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from agendamentos.views import agendamentos, agendar, deletar_agendamento, medico_view, medico_create, medico_delete, agenda_view, agenda_create, agenda_delete, especialidade_view, especialidade_create, especialidade_delete

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
]
