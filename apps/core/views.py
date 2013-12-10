from django.views.generic import TemplateView
from products.models import Product, Category


class BaseView(TemplateView):
    def get_categories(self):
        return Category.objects.all()

    def get_base_context(self):
        cxt = {}
        cxt['nodes'] = self.get_categories()

        return cxt


class IndexView(BaseView):
    template_name = 'core/index.html'

    def get_products(self):
        return Product.objects.all().select_related('category')

    def get(self, request, *args, **kwargs):
        products = self.get_products()

        cxt = self.get_base_context()
        cxt['products'] = products

        return self.render_to_response(cxt)
