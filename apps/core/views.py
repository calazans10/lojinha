from django.views.generic import TemplateView
from products.models import Product, Category


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_products(self):
        return Product.objects.all().select_related('category')

    def get_categories(self):
        return Category.objects.all()

    def get(self, request, *args, **kwargs):
        products = self.get_products()
        categories = self.get_categories()

        cxt = {}
        cxt['products'] = products
        cxt['nodes'] = categories

        return self.render_to_response(cxt)
