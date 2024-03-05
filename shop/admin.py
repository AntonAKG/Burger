from django.contrib import admin

from .models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    # list_filter = ('available', 'created', 'updated')
    # list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}
    # search_fields = ('name', 'description')
