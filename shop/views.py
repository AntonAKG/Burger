from django.views.generic import TemplateView, ListView

from shop.models import Product


class CatalogView(ListView):
    model = Product
    template_name = 'shop/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['products'] = Product.objects.all()
        return context


class ProductView(TemplateView):
    template_name = 'shop/product.html'
