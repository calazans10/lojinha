from django.views.generic import TemplateView
from products.models import Product, Category


class BaseView(TemplateView):
    def get_categories(self):
        return Category.objects.all()

    def get_products(self):
        return Product.objects.all().select_related('category')

    def get_base_context(self):
        cxt = {}
        cxt['nodes'] = self.get_categories()

        return cxt