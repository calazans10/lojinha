# -*- coding: utf-8 -*-
from core.views import BaseView
from products.models import Product


class ShowProduct(BaseView):
    template_name = 'products/show_product.html'

    def get(self, request, object_id, *args, **kwargs):
        product = Product.objects.get(pk=object_id)

        cxt = self.get_base_context()
        cxt['product'] = product

        return self.render_to_response(cxt)
