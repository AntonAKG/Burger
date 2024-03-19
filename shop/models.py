from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва категорії")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["id"]


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва продукту")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Зображення"
    )
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Ціна")
    discount = models.DecimalField(
        default=0, max_digits=9, decimal_places=2, verbose_name="Знижка"
    )
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Категорія"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def display_id(self):
        return f"{self.id:05}"
