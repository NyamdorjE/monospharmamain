from django.contrib import admin
from .models import Profile, PharmaProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "register", "license_number")
    search_fields = [
        "user",
        "phone",
        "register",
        "license_number",
        "organization_name",
        "category",
        "district",
    ]


admin.site.register(Profile, ProfileAdmin)


class PharmaProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "register", "license_number")
    search_fields = [
        "user",
        "phone",
        "register",
        "license_number",
        "organization_name",
        "category",
        "district",
    ]


admin.site.register(PharmaProfile, PharmaProfileAdmin)
