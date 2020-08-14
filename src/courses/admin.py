from django.contrib import admin
from src.courses.models import Subject, Lesson, Course, CourseCategory
# Register your models here.


# admin.site.register(Subject)
# admin.site.register(Course)
# admin.site.register(Lesson)
# admin.site.register(CourseCategory)
class InLineLesson(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    filter_horizontal = ('students',)
    list_display = ('title', 'description', 'price')
    list_filter = ('title',  'price')
    search_fields = ('title', 'slug')
    fieldsets = (
        (None, {
            "fields": (
                'category', 'title', 'price', 'description', 'image', 'students'
            ),
        }),
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory)
