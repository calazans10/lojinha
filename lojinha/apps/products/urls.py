# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from products.views import ShowProduct, ListProducts, ListItens


urlpatterns = patterns(
    '',
    url(r'show_product/(?P<object_id>[\d]+)$', ShowProduct.as_view(),
        name='show_product'),
    url(r'list_products/(?P<object_id>[\d]+)$', ListProducts.as_view(),
        name='list_products'),
    url(r'add_itens/(?P<object_id>[\d]+)$', 'products.views.add_itens',
        name='add_itens'),
    url(r'list_itens', ListItens.as_view(), name='list_itens')
)
