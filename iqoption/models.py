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

    object = models.Manager()


    def __str__(self):
        return self.name