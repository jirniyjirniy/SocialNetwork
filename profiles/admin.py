from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profiles.models import UserNet
from django.utils.translation import gettext_lazy as _



class UserNetAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', "middle_name", 'last_name', 'is_staff')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Info"), {"fields": ("phone", "avatar", "gender", "github", "bio", "birthday")}),
    )




admin.site.register(UserNet, UserNetAdmin)

