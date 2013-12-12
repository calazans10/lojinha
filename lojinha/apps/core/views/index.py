from core.views import BaseView


class IndexView(BaseView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        products = self.get_products()

        cxt = self.get_base_context()
        cxt['products'] = products

        return self.render_to_response(cxt)
