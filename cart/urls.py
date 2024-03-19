from django.urls import path

from .views import CartAddView

urlpatterns = [
    path("add/<slug:product_slug>/", CartAddView.as_view(), name="cart_add"),
]
