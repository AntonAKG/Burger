from django.db import models


class OrderitemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(item.product_price() for item in self)

    def total_quantity(self):
        if self:
            return sum(item.quantity for item in self)

        return 0


class Order(models.Model):
    user = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Користувач",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефон")
    address = models.TextField(null=True, blank=True, verbose_name="Адреса")
    requires_delivery = models.BooleanField(default=False, verbose_name="Доставка")
    payment = models.BooleanField(default=False, verbose_name="Оплата при отриманні")
    is_paid = models.BooleanField(default=False, verbose_name="Сплачено")
    status = models.CharField(max_length=50, default="В обробці", verbose_name="Статус")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення №{self.id} | Купець: {self.user.first_name} {self.user.last_name} | Статус: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        "shop.Product", on_delete=models.CASCADE, null=True, verbose_name="Товар"
    )
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Товар у замовленні"
        verbose_name_plural = "Товари у замовленні"

    objects = OrderitemQuerySet().as_manager()

    def __str__(self):
        return f"{self.product.name} у кількості {self.quantity} шт."

    def product_price(self):
        return self.product.price * self.quantity
