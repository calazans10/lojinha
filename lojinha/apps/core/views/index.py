# -*- coding: utf-8 -*-
from core.views import BaseView


class IndexView(BaseView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        products = self.get_products()

        cxt = self.get_context_data()
        cxt['products'] = products

        return self.render_to_response(cxt)
