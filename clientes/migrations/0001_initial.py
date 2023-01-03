# Generated by Django 4.1.5 on 2023-01-03 21:49

import cpf_field.models
import django.core.validators
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('mobile', models.CharField(max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Celular')),
                ('trader_brokerage', models.CharField(choices=[('iqoption', 'IQ Option')], default='iqoption', max_length=10, null=True, verbose_name='Corretora Trader')),
                ('user_name_brokerage', models.CharField(max_length=150, null=True, verbose_name='Usuário de Registro na Corretora')),
                ('email_brokerage', models.EmailField(max_length=254, null=True, verbose_name='E-mail de Registro na Corretora')),
                ('password_brokerage', models.CharField(max_length=128, null=True, verbose_name='Senha de Acesso na Corretora')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Data de Registro')),
                ('registration_date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Última Alteração')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
