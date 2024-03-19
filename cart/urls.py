from django.urls import path

from .views import CartAddView, CartRemoveView

urlpatterns = [
    path("add/<slug:product_slug>/", CartAddView.as_view(), name="cart_add"),
    path("remove/<int:cart_id>/", CartRemoveView.as_view(), name="cart_remove"),
]
