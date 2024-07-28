from django.contrib import admin
from .models import Product, Ingredient, Sale, Supplier



admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(Supplier)
admin.site.register(Sale)
