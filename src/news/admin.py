from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import News, Category, VideoNews, VideoNewsCategory
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author',
                    'created_on', 'is_special', 'category')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


admin.site.register(VideoNewsCategory)


class VideoNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category')
    search_fields = ['title', 'category']


admin.site.register(VideoNews, VideoNewsAdmin)
