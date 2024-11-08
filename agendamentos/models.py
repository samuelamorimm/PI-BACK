from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=65)
    email = models.CharField(verbose_name="Email", max_length=100)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    telefone = models.CharField(verbose_name='Telefone', max_length=11)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.nome

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

class Horario(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)

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
    
class ServicosAgendamentos(models.Model):
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE, verbose_name='Serviço')
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self) -> str:
        return str(self.id_servico)

class Agendamento(models.Model):
    STATUS_AGENDAMENTO = [
        ('P', 'PENDENTE'),
        ('A', 'EM ANDAMENTO'),
        ('F', 'FINALIZADO'),
    ]
    
    FORMA_PAGAMENTO = [
        ('ESPECIE', 'Espécie'),
        ('PIX', 'PIX'),
        ('CREDITO', 'Crédito'),
    ]

    nome_cliente = models.CharField(verbose_name="Nome", max_length=65)
    cpf_cliente = models.CharField(verbose_name="CPF", max_length=11)
    forma_pagamento = models.CharField(verbose_name='Forma de pagamento', choices=FORMA_PAGAMENTO, max_length=7, default='ESPECIE')
    status = models.CharField(verbose_name='Status', choices=STATUS_AGENDAMENTO, max_length=1, default='P')
    data = models.DateField(verbose_name='Data')
    registro = models.DateTimeField(auto_now_add=True)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')
    servico = models.ForeignKey(ServicosAgendamentos, on_delete=models.CASCADE, verbose_name="Serviço e Médico")
    horario_agendamento = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name='Horarios Disponiveis')

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self) -> str:
        return self.nome_cliente









