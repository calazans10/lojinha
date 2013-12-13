from django.views.generic import TemplateView
from products.models import Product, Category, Item


class BaseView(TemplateView):
    def get_categories(self):
        return Category.objects.all()

    def get_products(self):
        return Product.objects.all().select_related('category') \
            .order_by('created')

    def get_itens(self):
        return Item.objects.all().select_related('product')

    def get_base_context(self):
        cxt = {}
        cxt['nodes'] = self.get_categories()
        cxt['count_itens'] = self.get_itens().count()

        return cxt
