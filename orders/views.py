from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from cart.models import Cart
from .forms import CreateOrderForm
from .models import Order, OrderItem


class OrderCreateView(View):

    def get(self, request):
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

        return render(
            request,
            "orders/create_order.html",
            {"form": form, "title": "Оформлення замовлення"},
        )

    def post(self, request):
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():

            print("from is valid")
            try:
                with transaction.atomic():

                    print("transaction")
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            address=form.cleaned_data["address"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            payment=form.cleaned_data["payment"],
                        )

                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.price
                            quantity = cart_item.quantity

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                        cart_items.delete()

                        # print(form.cleaned_data["required_delivery"])

                        print(form.cleaned_data)
                        return redirect("profile")

            except ValidationError as e:
                print(e)
                return redirect("main_index")

        else:
            print(form.errors)
            initial = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
            form = CreateOrderForm(initial=initial)
            return render(
                request,
                "orders/create_order.html",
                {"form": form, "title": "Оформлення замовлення"},
            )
