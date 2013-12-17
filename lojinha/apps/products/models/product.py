# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from model_utils.models import TimeStampedModel
from metadata.models import MetaData


class Product(TimeStampedModel):
    code = models.CharField(u'Código', max_length=20)
    title = models.CharField(u'Título', max_length=120)
    description = models.CharField(u'Descrição', max_length=1500)
    price = models.DecimalField(u'Preço', max_digits=12, decimal_places=2)
    category = models.ForeignKey('Category', related_name='products',
                                 verbose_name=u'Categoria')
    quantity = models.IntegerField(u'Quantidade em estoque')
    photo = models.ImageField(u'Foto', upload_to='images/',
                              null=True, blank=True)
    metadata = generic.GenericRelation(MetaData)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'products'
        db_table = 'product'
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'
