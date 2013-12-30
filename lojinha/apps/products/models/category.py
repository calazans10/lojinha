# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(u'Nome', max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', verbose_name=u"Pai")

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        app_label = 'products'
        db_table = 'category'
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return self.name
