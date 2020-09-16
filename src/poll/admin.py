from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import Poll, Choice, Question


class InLineChoice(NestedTabularInline):
    model = Choice
    extra = 1


class InLineQuestion(NestedStackedInline):
    model = Question
    inlines = [InLineChoice]
    extra = 1


class PollAdmin(NestedModelAdmin):
    inlines = [InLineQuestion]


admin.site.register(Poll, PollAdmin)


admin.site.register(Question)

admin.site.register(Choice)