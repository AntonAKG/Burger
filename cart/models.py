from django.db import models

from account.models import User
from shop.models import Product


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(item.product_price() for item in self)

    def total_quantity(self):
        if self:
            return sum(item.quantity for item in self)

        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Користувач"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Кількість")
    session_key = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="Ключ сесії"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    objects = CartQuerySet().as_manager()

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"

    def product_price(self):
        return self.product.price * self.quantity
