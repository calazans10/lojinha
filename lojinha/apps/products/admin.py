# -*- coding: utf-8 -*-
from django.contrib import admin
from metadata.admin import MetaDataTabularInline
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'title', 'price', 'category',)
    list_select_related = ('category',)
    search_fields = ['code', 'title', 'description']
    inlines = [MetaDataTabularInline]

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
