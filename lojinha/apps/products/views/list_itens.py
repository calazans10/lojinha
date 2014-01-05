# -*- coding: utf-8 -*-
from django.db.models import Sum
from core.views import BaseView


class ListItens(BaseView):
    template_name = 'products/list_itens.html'

    def get(self, request, *args, **kwars):
        itens = self.get_itens()

        cxt = self.get_context_data()
        cxt['itens'] = itens
        cxt['sum_price'] = itens.aggregate(sum=Sum('price'))['sum']

        return self.render_to_response(cxt)
