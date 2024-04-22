# Generated by Django 5.0.2 on 2024-04-18 08:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата створення"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="Номер телефон"),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="Адреса"),
                ),
                (
                    "payment",
                    models.BooleanField(
                        default=False, verbose_name="Оплата при отриманні"
                    ),
                ),
                (
                    "is_paid",
                    models.BooleanField(default=False, verbose_name="Сплачено"),
                ),
                (
                    "status",
                    models.CharField(
                        default="В обробці", max_length=50, verbose_name="Статус"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Користувач",
                    ),
                ),
            ],
            options={
                "verbose_name": "Замовлення",
                "verbose_name_plural": "Замовлення",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Назва")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Ціна"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="Кількість"),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата створення"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                        verbose_name="Замовлення",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар у замовленні",
                "verbose_name_plural": "Товари у замовленні",
            },
        ),
    ]
