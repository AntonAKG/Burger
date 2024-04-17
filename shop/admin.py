from django.contrib import admin

from .models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("price",)
    search_fields = ("name",)
    list_filter = ("category", "price")
    fields = ("name", "category", "price", "slug", "description", "image")
