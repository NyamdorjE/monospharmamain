from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'register',
                    'license_number')
    search_fields = ['user', 'phone', 'register',
                     'license_number', 'organization_name', 'category', 'district']


admin.site.register(Profile, ProfileAdmin)
