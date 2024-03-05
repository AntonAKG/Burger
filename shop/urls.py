from django.urls import path

from .views import CatalogView, ProductDetailView

urlpatterns = [
    path('catalog/<slug:category_slug>', CatalogView.as_view(), name='catalog'),
    # path('catalog/product', ProductView.as_view(), name='product'),
    path('catalog/product/<slug:slug>', ProductDetailView.as_view(), name='product'),
]