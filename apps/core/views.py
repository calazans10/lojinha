from django.views.generic import TemplateView
from products.models import Product


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_products(self):
        return Product.objects.all().select_related('category')

    def get(self, request, *args, **kwargs):
        products = self.get_products()

        cxt = {}
        cxt['products'] = products

        return self.render_to_response(cxt)
