from django.contrib import admin

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    ordering = (
        "email",
        "id",
    )

    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "status",
        "is_donor",
        "is_receipient",
        "blood_group",
        # "is_staff",
        # "is_superuser",
        # "is_active",
    )

    search_fields = ("first_name", "last_name", "email", "phone",)

    list_filter = ("is_staff", "is_active")

    # list_editable = ("is_staff", "is_superuser", "is_active")

    exclude = ("username", "date_joined")

    add_fieldsets = (
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Contact Info",
            {
                "fields": ("email","address","phone", ),
            },
        ),
        (
            "Password",
            {
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    fieldsets = (
        (
            "Contact Info",
            {
                "fields": (
                    "email",
                    "address",
                    "phone",
                )
            },
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
                "classes": ["wide", "extrapretty"],
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            },
        ),
        ("Password", {"fields": ("password",)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Bloodstock)
admin.site.register(Order)
admin.site.register(Blooddonation)
admin.site.register(Offlinedelivery)