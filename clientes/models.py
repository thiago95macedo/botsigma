from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField


class Cliente(models.Model):
    name = models.CharField('Nome', max_length=150, null=True)
    cpf = CPFField('CPF', null=True)
    TRADER_BROKERAGE_CHOICES = (
        ('iqoption', 'IQ Option'),
    )
    trader_brokerage = models.CharField('Corretora Trader', max_length=10, choices=TRADER_BROKERAGE_CHOICES, default='iqoption')
    user_name_brokerage = models.CharField('Usuário de Registro na Corretora', max_length=150, null=True)
    email_brokerage = models.EmailField('E-mail de Registro na Corretora', max_length=254, null=True)
    password_brokerage = models.CharField('Senha de Acesso na Corretora', max_length=128, null=True)
    registration_date = models.DateTimeField('Data de Registro', default=timezone.now)


    def __str__(self):
        return self.name