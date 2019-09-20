from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'count', 'price']
    list_filter = ['category']
    list_display_links = ['name']
    search_fields = ['category']
    exclude = []


admin.site.register(Product, ProductAdmin)

