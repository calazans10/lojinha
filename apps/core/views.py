from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        cxt = {}

        return self.render_to_response(cxt)
