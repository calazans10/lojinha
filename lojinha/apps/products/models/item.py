# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Item(TimeStampedModel):
    product = models.ForeignKey('Product', related_name='items',
                                verbose_name=u'Produto')
    quantity = models.IntegerField(u'Quantidade')
    price = models.DecimalField(u'Preço', max_digits=12, decimal_places=2)

    class Meta:
        app_label = 'products'
        db_table = 'item'
        verbose_name = u'Item'
        verbose_name_plural = u'Itens'
