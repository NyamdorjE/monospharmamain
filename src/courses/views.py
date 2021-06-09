from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.models import User

from src.courses.models import Subject, Lesson, Course, CourseCategory
from src.chat.models import Message


class HomeView(ListView):
    template_name = "course.html"
    queryset = Course.objects.all()
    paginate_by = 6

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_queryset()
        context["categorylist"] = CourseCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(HomeView, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset


class AboutView(TemplateView):
    template_name = "about.html"


def CourseListView(request, category):
    courses = Subject.objects.filter(course=category)
    category = Course.objects.all()
    context = {
        "courses": courses,
        "category": category,
    }
    return render(request, "courses/course_list.html", context)


class CourseDetailView(DetailView):
    context_object_name = "course"
    template_name = "courses/course_detail.html"
    model = Subject


class SuggestView(TemplateView):
    template_name = "request.html"


class LessonDetailView(FormView, LoginRequiredMixin):
    template_name = "courses/lesson_detail.html"
    success_url = "/thanks/"

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        lesson1 = get_object_or_404(Lesson, slug=lesson_slug)
        username = User.objects.filter(id=request.user.id).first()
        messages = Message.objects.filter(lesson=lesson1)[0:25]

        subject = get_object_or_404(Subject, slug=course_slug)
        student_ids = Course.objects.get(pk=subject.course.id).students.values_list(
            "id", flat=True
        )
        if request.user.id in list(student_ids):
            course = get_object_or_404(Subject, slug=course_slug)

            lesson = get_object_or_404(Lesson, slug=lesson_slug)

            context = {
                "name": username,
                "messages": messages,
                "lesson": lesson,
                "course": course,
            }
            return render(request, "courses/lesson_detail.html", context)
        else:
            return redirect("courses:suggest")


@login_required
def SearchView(request):
    if request.method == "POST":
        search = request.POST.get("search")
        results = Lesson.objects.filter(title__contains=search)
        context = {"results": results}
        return render(request, "courses/search_result.html", context)
