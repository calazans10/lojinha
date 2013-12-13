# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from products.models import Product, Item


def add_itens(request, object_id):
    product = Product.objects.get(pk=object_id)
    item = Item(product=product, quantity=1, price=product.price)
    item.save()

    return redirect('index')
