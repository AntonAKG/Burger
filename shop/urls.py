from django.urls import path

from .views import CatalogView, ProductDetailView

urlpatterns = [
    path('catalog/<slug:category_slug>', CatalogView.as_view(), name='catalog'),
    path('search/', CatalogView.as_view(), name='search'),
    path('catalog/product/<slug:slug>', ProductDetailView.as_view(), name='product'),
]