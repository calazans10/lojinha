from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.ForeignKey(User)
    cpf = models.CharField(max_length=14)
    born_on = models.DateField()

    class Meta:
        app_label = 'clients'
        db_table = 'client'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
