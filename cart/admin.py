from django.contrib import admin

from .models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("product", "quantity", "created_at")
    readonly_fields = ("created_at",)

    extra = 1


@admin.register(Cart)
class UserAdmin(admin.ModelAdmin):
    # list_display = ("first_name", "last_name", "email", "is_staff")
    list_display = ("user", "product", "quantity", "created_at")
    list_filter = ("user", "product__name", "created_at")
