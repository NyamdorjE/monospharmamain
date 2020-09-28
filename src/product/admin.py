from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Product, ProductCategory,  Type, ProductForm

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_product_new')
    search_fields = ('name',)
    list_filter = ['categories']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory)
# admin.site.register(Classification)
admin.site.register(Type)
admin.site.register(ProductForm)
