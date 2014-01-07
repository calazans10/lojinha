# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy


class ProductTest(TestCase):
    def setUp(self):
        category = mommy.make('Category', name='Livro')
        self.product = mommy.make('Product', title="Livro Exemplo",
                                  category=category)

    def test_unicode_representation(self):
        self.assertEqual(unicode(self.product), self.product.title)
