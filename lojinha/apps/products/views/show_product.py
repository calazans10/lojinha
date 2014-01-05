# -*- coding: utf-8 -*-
from products.models import Product
from core.views import BaseView


class ShowProduct(BaseView):
    template_name = 'products/show_product.html'

    def get(self, request, object_id, *args, **kwargs):
        product = Product.objects.get(pk=object_id)

        cxt = self.get_context_data()
        cxt['product'] = product

        return self.render_to_response(cxt)
