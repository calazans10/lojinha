from core.views import BaseView
from .models import Category


class ListProducts(BaseView):
    template_name = 'products/list_products.html'

    def filter_products(self, category):
        products = self.get_products().filter(category=category)
        return products

    def get(self, request, object_id, *args, **kwargs):
        category = Category.objects.get(pk=object_id)
        products = self.filter_products(category)

        cxt = self.get_base_context()
        cxt['category'] = category
        cxt['products'] = products

        return self.render_to_response(cxt)
