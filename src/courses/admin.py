from django.contrib import admin
from src.courses.models import Subject, Lesson, Course, CourseCategory
from nested_inline.admin import (
    NestedStackedInline,
    NestedModelAdmin,
    NestedTabularInline,
)

# Register your models here.


# admin.site.register(Subject)
# admin.site.register(Course)
# admin.site.register(Lesson)
admin.site.register(CourseCategory)


class InLineLesson(NestedTabularInline):
    model = Lesson
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


class InLineSubject(NestedTabularInline):
    inlines = [InLineLesson]
    prepopulated_fields = {"slug": ("title",)}
    model = Subject
    extra = 0


class InLineCourse(NestedModelAdmin):
    inlines = [InLineSubject]
    filter_horizontal = ("students",)
    search_fields = ("title", "slug")
    list_filter = ("category", "price")
    list_display = ("title", "description", "price", "state")


admin.site.register(Course, InLineCourse)