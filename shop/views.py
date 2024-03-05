from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from shop.models import Product


class CatalogView(ListView):
    model = Product
    template_name = 'shop/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['category_slug'] == 'all':
            context['products'] = Product.objects.all()
        else:
            context['products'] = get_object_or_404(Product.objects.filter(category__slug=self.kwargs['category_slug']))

        context['title'] = 'Каталог'
        return context


# class ProductView(TemplateView):
#     template_name = 'shop/product.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    slug_field = 'product_slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        return context

