from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    Product,
    ProductCategory,
    Type,
    ProductForm,
)
from .fetch import product_emonos

from mptt.admin import (
    DraggableMPTTAdmin,
    TreeRelatedFieldListFilter,
)  # Register your models here.


class ProductCategoryFilter(admin.SimpleListFilter):
    title = "Ангилал"

    parameter_name = "category"

    def lookups(self, request, model_admin):
        return (
            ("has_category", "Ангилалтай"),
            ("no_category", "Ангилалгүй"),
        )

    def queryset(self, request, queryset):
        if self.value() == "has_category":
            return queryset.exclude(categories=None)
        if self.value() == "no_category":
            return queryset.filter(categories=None)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "is_product_new", "get_parents")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("categories",)

    list_filter = [
        ProductCategoryFilter,
    ]

    def action_product(self, request, queryset):
        product_emonos()
        self.message_user(request, "Бүтээгдэхүүний мэдээлэл амжилттай татагдлаа.")


@admin.register(ProductCategory)
class ProductCategoryAdmin(DraggableMPTTAdmin):
    """
    Product Category
    """

    list_display_links = ("indented_title",)
    list_display = ["tree_actions", "indented_title"]
    mptt_indent_field = "name"
    prepopulated_fields = {"slug": ("name",)}
    search_fields = [
        "name",
    ]


# admin.site.register(Classification)
admin.site.register(Type)
admin.site.register(ProductForm)
