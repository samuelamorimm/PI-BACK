from django.db import models

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=65)
    especialidade = models.CharField(verbose_name='Especialidade', max_length=65)
    email = models.CharField(verbose_name='Email', max_length=100)
    telefone = models.CharField(verbose_name="Telefone", max_length=11)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self) -> str:
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    tipo_servico = [
        'ESTETICO',
        'ODONTO'
    ]
    preco = models.FloatField()
    descricao = models.TextField()
    duracao_estimativa = models.DateTimeField()

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return self.nome

class Agendamento(models.Model):
    STATUS_AGENDAMENTO = [
        ('P', 'PENDENTE'),
        ('A', 'EM ANDAMENTO'),
        ('F', 'FINALIZADO'),
    ]
    
    forma_pagamento = [
        'ESPECIE',
        'PIX',
        'CREDITO'
    ]


    status = models.CharField(verbose_name='Status', choices=STATUS_AGENDAMENTO, max_length=1)
    data_hora = models.DateTimeField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add=True)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self) -> str:
        return 'Agendamento'

class ServicosAgendamentos(models.Model):
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    id_agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.descricao







