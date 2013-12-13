# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from metadata.admin import MetaDataTabularInline
from products.models import Product, Category


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('id', 'code', 'title', 'price', 'category',)
    list_select_related = ('category',)
    search_fields = ['code', 'title', 'description']
    inlines = [MetaDataTabularInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
