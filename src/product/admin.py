from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Product, ProductCategory, Type, ProductForm
from .fetch import product_emonos

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "web_category", "is_product_new")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def action_product(self, request, queryset):
        product_emonos()
        self.message_user(request, "Бүтээгдэхүүний мэдээлэл амжилттай татагдлаа.")


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory)
# admin.site.register(Classification)
admin.site.register(Type)
admin.site.register(ProductForm)
