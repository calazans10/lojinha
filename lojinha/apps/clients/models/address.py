from django.db import models
from model_utils.models import TimeStampedModel


class Address(TimeStampedModel):
    street = models.CharField('Rua', max_length=100)
    number = models.IntegerField('Número')
    neighborhood = models.CharField('Bairro', max_length=100)
    zipcode = models.CharField('CEP', max_length=9)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)

    def get_full_address(self):
        string = 'Rua: {:s} - Nº: {:d} - Bairro: {:s} - CEP: {:s}'
        return string.format(self.street, self.number, self.neighborhood,
                             self.zipcode)

    def __str__(self):
        return self.get_full_address()

    class Meta:
        app_label = 'clients'
        db_table = 'address'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
