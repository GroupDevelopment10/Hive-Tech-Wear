from django.contrib import admin

# Register your models here.
from .models import Product

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    fields = ['name', 'description', 'price','image','type', 'category']
    list_filter = []
    list_display = fields
    search_fields = ['name', 'description']