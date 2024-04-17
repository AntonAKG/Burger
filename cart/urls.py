from django.urls import path

from .views import CartAddView, CartRemoveView, CartChangeView

urlpatterns = [
    path("add/", CartAddView.as_view(), name="cart_add"),
    path("remove/", CartRemoveView.as_view(), name="cart_remove"),
    path("change/", CartChangeView.as_view(), name="cart_change"),
]
