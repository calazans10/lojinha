from django.conf.urls import patterns, url
from products.views import ShowProduct, ListProducts


urlpatterns = patterns(
    '',
    url(r'show_product/(?P<object_id>[\d]+)$', ShowProduct.as_view(),
        name='show_product'),
    url(r'list_products/(?P<object_id>[\d]+)$', ListProducts.as_view(),
        name='list_products'),
)
