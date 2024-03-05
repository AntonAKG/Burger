from django.urls import path

from .views import CatalogView, ProductView

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/product', ProductView.as_view(), name='product'),
]