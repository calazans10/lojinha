from django.db import models


class Client(models.Model):
    user = models.OneToOneField('auth.User', related_name="client")
    cpf = models.CharField(max_length=14)
    born_on = models.DateField()

    class Meta:
        app_label = 'clients'
        db_table = 'client'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
