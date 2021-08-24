from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    Product,
    ProductCategory,
    ProductCategoryImage,
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


# @admin.register(ProductCategory)
# class ProductCategoryAdmin(DraggableMPTTAdmin):
#     """
#     Product ProductCategory
#     """

#     list_display_links = ("indented_title",)
#     list_display = [
#         "tree_actions",
#         "indented_title",
#         "related_products_count",
#         "related_products_cumulative_count",
#     ]
#     mptt_indent_field = "name"
#     prepopulated_fields = {"slug": ("name",)}
#     search_fields = [
#         "name",
#     ]

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)

#         # Add cumulative product count
#         qs = ProductCategory.objects.add_related_count(
#             qs, Product, "categories", "products_cumulative_count", cumulative=True
#         )

#         # Add non cumulative product count
#         qs = ProductCategory.objects.add_related_count(
#             qs, Product, "categories", "products_count", cumulative=False
#         )
#         return qs

#     def related_products_count(self, instance):
#         return instance.products_count

#     related_products_count.short_description = (
#         "Related products (for this specific category)"
#     )

#     def related_products_cumulative_count(self, instance):
#         return instance.products_cumulative_count

#     related_products_cumulative_count.short_description = "Related products (in tree)"


# admin.site.register(Classification)
admin.site.register(Type)
admin.site.register(ProductForm)
admin.site.register(ProductCategoryImage)
