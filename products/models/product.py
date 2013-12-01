from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    code = models.CharField('Código', max_length=20)
    description = models.CharField('Descrição', max_length=255)
    price = models.DecimalField('Preço', max_digits=12, decimal_places=2)
    category = models.ForeignKey('Category', related_name='products',
                                 verbose_name='Categoria')

    class Meta:
        app_label = 'products'
        db_table = 'product'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
