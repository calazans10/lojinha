# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from products.models import Product


class ProductQuerySetTest(TestCase):
    def setUp(self):
        self.category = mommy.make('Category', name='Livro')
        self.product = mommy.make('Product', title="Livro Exemplo",
                                  category=self.category)

    def test_by_category(self):
        queryset = Product.objects.by_category(self.category)

        self.assertIn(self.product, queryset)
