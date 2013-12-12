from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    user = models.OneToOneField('auth.User', verbose_name="Usuário")
    cpf = models.CharField('CPF', max_length=14)
    born_on = models.DateField('Nascido em')
    addresses = models.ManyToManyField('Address', verbose_name="Endereços")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        app_label = 'clients'
        db_table = 'client'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
