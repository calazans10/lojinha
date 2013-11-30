from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    user = models.OneToOneField('auth.User', verbose_name="Usuário")
    cpf = models.CharField('CPF', max_length=14)
    born_on = models.DateField('Nascido em')
    addresses = models.ManyToManyField('Address', verbose_name="Endereços")

    class Meta:
        app_label = 'clients'
        db_table = 'client'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Address(TimeStampedModel):
    street = models.CharField('Rua', max_length=100)
    neighborhood = models.CharField('Bairro', max_length=100)
    zipcode = models.CharField('CEP', max_length=9)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)

    class Meta:
        app_label = 'clients'
        db_table = 'address'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
