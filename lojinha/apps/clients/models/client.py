# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    user = models.OneToOneField('auth.User', verbose_name=u"Usuário")
    cpf = models.CharField(u'CPF', max_length=14)
    born_on = models.DateField(u'Data de nascimento')
    addresses = models.ManyToManyField('Address', verbose_name=u"Endereços")

    class Meta:
        app_label = 'clients'
        db_table = 'client'
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'

    def __unicode__(self):
        return self.user.get_full_name()
