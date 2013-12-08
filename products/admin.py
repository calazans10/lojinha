from django.contrib import admin
from metadata.admin import MetaDataTabularInline
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    inlines = [MetaDataTabularInline]


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
