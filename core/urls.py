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
from django.urls import path
from agendamentos.views import agendamentos, agendar, deletar_agendamento, medicos, add_medico, medico_delete, agendas, add_agenda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agendamentos, name='agendamentos'),
    path('agendar/', agendar, name='agendar'),
    path('deletar/<int:id>', deletar_agendamento, name='deletar_agendamento'),
    path('medico/', medicos, name='medicos'),
    path('adicionarmed/', add_medico, name='add_medico'),
    path('deletemed/<int:id>', medico_delete, name='medico_delete'),
    path('agenda/', agendas, name='agendas'),
    path('addagenda/', add_agenda, name='add_agenda')
]
