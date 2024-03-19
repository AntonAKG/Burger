from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View

from shop.models import Product
from .models import Cart


class CartAddView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        product_slug = kwargs["product_slug"]
        product = get_object_or_404(Product, slug=product_slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META["HTTP_REFERER"])
