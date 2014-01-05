# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.query import QuerySet
from django.contrib.contenttypes import generic
from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from metadata.models import MetaData


class ProductQuerySet(QuerySet):
    def by_category(self, category):
        return self.filter(category=category)


class Product(TimeStampedModel):
    code = models.CharField(u'Código', max_length=20)
    title = models.CharField(u'Título', max_length=120)
    description = models.TextField(u'Descrição')
    price = models.DecimalField(u'Preço', max_digits=12, decimal_places=2)
    category = models.ForeignKey('Category', related_name='products',
                                 verbose_name=u'Categoria')
    quantity = models.IntegerField(u'Quantidade em estoque')
    photo = models.ImageField(u'Foto', upload_to='images/',
                              null=True, blank=True)
    metadata = generic.GenericRelation(MetaData)
    objects = PassThroughManager.for_queryset_class(ProductQuerySet)()

    class Meta:
        app_label = 'products'
        db_table = 'product'
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'

    def __unicode__(self):
        return self.title
