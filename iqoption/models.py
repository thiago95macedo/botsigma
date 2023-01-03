from django.db import models
from django.utils import timezone


class IqOption(models.Model):
    name = models.CharField('Nome', max_length=150, blank=False, null=True)
    


    def __str__(self):
        return self.name