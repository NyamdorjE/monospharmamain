from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Product, ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)