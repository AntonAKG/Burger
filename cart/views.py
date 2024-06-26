from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View
import json
from shop.models import Product
from .models import Cart
from .utils import get_user_carts


class CartAddView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        request.session.set_expiry(0)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        else:
            carts = Cart.objects.filter(
                session_key=request.session.session_key, product=product
            )

            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(
                    session_key=request.session.session_key, product=product, quantity=1
                )

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


class CartRemoveView(View):
    """
    Remove a product from the cart
    """

    @staticmethod
    def post(request, *args, **kwargs):
        cart_id = request.POST.get("cart-id")

        cart = Cart.objects.get(id=cart_id)
        cart.delete()

        return HttpResponseRedirect(request.META["HTTP_REFERER"])


class CartChangeView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            cart_id = data.get("cart-id")
            quantity = data.get("quantity")

            print("cart_id:", cart_id)
            print("quantity:", quantity)

            if cart_id is not None and quantity is not None:
                cart = Cart.objects.get(id=cart_id)
                cart.quantity = quantity
                cart.save()
                updated_quantity = cart.quantity

                cart = get_user_carts(request)
                cart_items_html = render_to_string(
                    "cart/includes/included_cart.html", {"carts": cart}, request=request
                )

                response_data = {
                    "message": "Кількість товару змінено!",
                    "cart_items_html": cart_items_html,
                    "quaantity": updated_quantity,
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({"message": "Invalid data"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
