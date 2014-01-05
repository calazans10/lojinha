# -*- coding: utf-8 -*-
from products.models import Category
from core.views import BaseView


class ListProducts(BaseView):
    template_name = 'products/list_products.html'

    def get(self, request, object_id, *args, **kwargs):
        category = Category.objects.get(pk=object_id)
        products = self.get_products().by_category(category)

        cxt = self.get_context_data()
        cxt['category'] = category
        cxt['products'] = products

        return self.render_to_response(cxt)
