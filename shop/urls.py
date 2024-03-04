from django.urls import path

from .views import Catalog, Product

urlpatterns = [
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('catalog/product', Product.as_view(), name='product'),
]