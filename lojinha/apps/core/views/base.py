# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from products.models import Product, Category, Item


class BaseView(TemplateView):
    def get_categories(self):
        return Category.objects.all()

    def get_products(self):
        qs = Product.objects.all().select_related('category')
        return qs.order_by('created')

    def get_itens(self):
        return Item.objects.all().select_related('product')

    def get_context_data(self, **kwargs):
        cxt = super(BaseView, self).get_context_data(**kwargs)
        cxt['nodes'] = self.get_categories()
        cxt['count_itens'] = self.get_itens().count()

        return cxt
