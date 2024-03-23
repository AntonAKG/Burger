from typing import Any

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView

from shop.models import Product
from .models import Cart
from .utils import get_user_carts


class CartAddView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        # print(*request.GET)
        print(*request.POST)
        product_id = request.POST.get("product_id")
        print(product_id)
        # product = get_object_or_404(Product, slug=product_id)
        product = Product.objects.get(id=product_id)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        user_cart = get_user_carts(request)
        print(user_cart)

        cart_items_html = render_to_string(
            "cart/includes/included_cart.html", {"cart": user_cart}, request=request
        )
        print(cart_items_html)

        responce_data: dict[str, str | Any] = {
            "message": "Product added to cart",
            "cart_items_html": cart_items_html,
        }

        return JsonResponse(responce_data)


class CartRemoveView(View):
    """
    Remove a product from the cart
    """

    @staticmethod
    def get(request, *args, **kwargs):
        cart = get_object_or_404(Cart, id=kwargs["cart_id"])
        cart.delete()
        return redirect(request.META["HTTP_REFERER"])
