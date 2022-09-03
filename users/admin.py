from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = (
        "email",
        "username",
    )
    list_display_links = ("email",)
    list_filter = ("id", "email", "username", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("id", "email", "username", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {"fields": ("email", "username", "first_name", "last_name", "middle_name")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        (
            "Personal",
            {
                "fields": (
                    "about",
                    "living_place",
                    "ware_house",
                    "delivery_type",
                    "phone",
                )
            },
        ),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(NewUser, UserAdminConfig)
