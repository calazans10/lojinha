from django.db import models
from model_utils.models import TimeStampedModel


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
