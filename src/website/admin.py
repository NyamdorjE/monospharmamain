from django.contrib import admin
from .models import (
    Advice,
    AdviceCategory,
    Testimonail,
    Gallery,
    FeaturedProduct,
    Banner,
    BannerVideo,
)

# Register your models here.


class AdviceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created_on", "category")
    search_fields = ["title", "category"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Advice, AdviceAdmin)
admin.site.register(AdviceCategory)
admin.site.register(Testimonail)
admin.site.register(Gallery)
admin.site.register(FeaturedProduct)
admin.site.register(Banner)
admin.site.register(BannerVideo)