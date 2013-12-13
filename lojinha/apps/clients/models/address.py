# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Address(TimeStampedModel):
    street = models.CharField(u'Rua', max_length=100)
    number = models.IntegerField(u'Número')
    neighborhood = models.CharField(u'Bairro', max_length=100)
    zipcode = models.CharField(u'CEP', max_length=9)
    city = models.CharField(u'Cidade', max_length=100)
    state = models.CharField(u'Estado', max_length=100)

    def get_full_address(self):
        string = u'Rua: {:s} - Nº: {:d} - Bairro: {:s} - CEP: {:s}'
        return string.format(self.street, self.number, self.neighborhood,
                             self.zipcode)

    def __unicode__(self):
        return self.get_full_address()

    class Meta:
        app_label = 'clients'
        db_table = 'address'
        verbose_name = u'Endereço'
        verbose_name_plural = u'Endereços'
