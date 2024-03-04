from django.views.generic import TemplateView


class Catalog(TemplateView):
    template_name = 'shop/catalog.html'


class Product(TemplateView):
    template_name = 'shop/product.html'
