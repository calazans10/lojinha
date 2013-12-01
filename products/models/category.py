from django.db import models
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField('Nome', max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', verbose_name="Pai")

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        app_label = 'products'
        db_table = 'category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
