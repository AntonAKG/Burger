from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView, DetailView

from shop.models import Product


class CatalogView(ListView):
    model = Product
    template_name = 'shop/catalog.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        on_sale = self.request.GET.get('on_sale', None)
        order_by = self.request.GET.get('order_by', None)

        if self.kwargs['category_slug'] == 'all':
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category__slug=self.kwargs['category_slug'])

        if on_sale:
            products = products.filter(discount__gt=0)

        if order_by and order_by != 'default':
            products = products.order_by(order_by)

        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        context['products'] = page_obj
        context['title'] = 'Каталог'
        context['slug'] = self.kwargs['category_slug']
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        return context
