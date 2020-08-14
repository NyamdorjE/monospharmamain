import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from src.courses.models import Subject, Lesson, Course, CourseCategory
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


# Create your views here.

class HomeView(TemplateView):
    template_name = 'course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Course.objects.all()
        context['category'] = category
        context['categorylist'] = CourseCategory.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


def CourseListView(request, category):
    courses = Subject.objects.filter(course=category)
    context = {
        'courses': courses
    }
    return render(request, 'courses/course_list.html', context)


class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    model = Subject


class SuggestView(TemplateView):
    template_name = "request.html"


class LessonDetailView(View, LoginRequiredMixin):

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        courses = Course.objects.all()
        subject = get_object_or_404(Subject, slug=course_slug)
        student_ids = Course.objects.get(
            pk=subject.course.id).students.values_list('id', flat=True)
        print(list(student_ids), '**************')
        if request.user.id in list(student_ids):
            course = get_object_or_404(Subject, slug=course_slug)
            lesson = get_object_or_404(Lesson, slug=lesson_slug)
            context = {'lesson': lesson, 'course': course}
            return render(request, "courses/lesson_detail.html", context)
        else:
            return redirect('courses:suggest')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject"] = Subject.objects.all()
        return context


# def get(self,request,course_slug,lesson_slug,*args,**kwargs):
#
#     course_qs = Course.objects.filter(slug=course_slug)
#     if course_qs.exists():
#         course = course_qs.first()
#     lesson_qs = course.lessons.filter(slug=lesson_slug)
#     if lesson_qs.exists():
#         lesson = lesson_qs.first()
#     user_membership = UserMembership.objects.filter(user=request.user).first()
#     user_membership_type = user_membership.membership.membership_type
#
#     course_allowed_membership_type = course.allowed_memberships.all()
#     context = {'lessons':None}
#
#     if course_allowed_membership_type.filter(membership_type=user_membership_type).exists():
#         context = {'lesson':lesson}
#
#     return render(request,'courses/lesson_detail.html',context)


@login_required
def SearchView(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Lesson.objects.filter(title__contains=search)
        context = {
            'results': results
        }
        return render(request, 'courses/search_result.html', context)
