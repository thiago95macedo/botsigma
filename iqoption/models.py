from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from cpf_field.models import CPFField


class Iqoption(models.Model):
    name = models.CharField(
        'Nome', 
        max_length=150, 
        blank=False, 
        null=True
    )

    cpf = CPFField(
        'CPF', 
        unique=True, 
        blank=False, 
        null=True    
    )

    mobileRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    mobile = models.CharField(
        'Celular',
        validators = [mobileRegex],
        max_length=16,
        unique=False, 
        blank=False, 
        null=True    
    )

    TRADER_BROKERAGE_CHOICES = (
        ('iqoption', 'IQ Option'),
    )
    trader_brokerage = models.CharField(
        'Corretora Trader', 
        max_length=10, 
        choices=TRADER_BROKERAGE_CHOICES, 
        blank=False, 
        null=True, 
        default='iqoption')

    user_name_brokerage = models.CharField(
        'Usuário de Registro na Corretora', 
        max_length=150, 
        blank=False, 
        null=True
    )

    email_brokerage = models.EmailField(
        'E-mail de Registro na Corretora', 
        max_length=254, 
        blank=False, 
        null=True
    )

    password_brokerage = models.CharField(
        'Senha de Acesso na Corretora',
         max_length=128, 
         blank=False, 
         null=True
    )

    registration_date = models.DateTimeField(
        'Data de Registro', 
        default=timezone.now, 
        blank=False, 
        null=True
    )

    registration_date_update = models.DateTimeField(
        'Última Alteração', 
        auto_now=True, 
        blank=False, 
        null=True
    )

    object = models.Manager()


    def __str__(self):
        return self.name