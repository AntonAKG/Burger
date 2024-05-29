from django.contrib import admin

from cart.admin import CartTabAdmin
from .models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_staff")

    inlines = [
        CartTabAdmin,
    ]

