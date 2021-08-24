from django.contrib import admin
from .models import (
    AboutUsCards,
    Advice,
    AdviceCategory,
    BannerAboutUs,
    HrBanner,
    Testimonail,
    Gallery,
    LeftFeaturedProduct,
    RightFeaturedProduct,
    Banner,
    BannerVideo,
    Counter,
)

# Register your models here.


class AdviceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created_on", "category")
    search_fields = ["title", "category"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Counter)
admin.site.register(BannerAboutUs)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(AdviceCategory)
admin.site.register(Testimonail)
admin.site.register(Gallery)
admin.site.register(LeftFeaturedProduct)
admin.site.register(RightFeaturedProduct)
admin.site.register(Banner)
admin.site.register(BannerVideo)
admin.site.register(AboutUsCards)
admin.site.register(HrBanner)
