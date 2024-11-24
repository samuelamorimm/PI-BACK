from django.db import models

# Create your models here.
    
class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return self.nome

class Medico(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=65)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, verbose_name='Especialidade', max_length=65)
    email = models.CharField(verbose_name='Email', max_length=100)
    telefone = models.CharField(verbose_name="Telefone", max_length=11)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self) -> str:
        return self.nome

    
class ServicosAgendamentos(models.Model):
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, verbose_name='Especialidade')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico')
    data = models.DateField(verbose_name='Data')

    HORARIOS_AGENDAMENTOS = [
        ('08:00 - 09:00', '08:00 - 09:00'),
        ('09:00 - 10:00', '09:00 - 10:00'),
        ('10:00 - 11:00', '10:00 - 11:00'),
        ('11:00 - 12:00', '11:00 - 12:00'),
        ('12:00 - 13:00', '12:00 - 13:00'),
        ('13:00 - 14:00', '13:00 - 14:00'),
        ('14:00 - 15:00', '14:00 - 15:00'),
    ]
    
    horario = models.CharField(verbose_name='Horário', choices=HORARIOS_AGENDAMENTOS, default='1', max_length=13)
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self) -> str:
        return f'{self.especialidade} - {self.medico} - {self.horario}'
    
    

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
    servico = models.ForeignKey(ServicosAgendamentos, on_delete=models.CASCADE, verbose_name="Serviço, Médico e Horário disponiveis")

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self) -> str:
        return self.nome_cliente









