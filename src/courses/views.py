import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from src.courses.models import Subject, Lesson, Course, CourseCategory
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


# Create your views here.

class HomeView(TemplateView):
    template_name = 'course.html'
    paginate_by = 2

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


class LessonDetailView(FormView, LoginRequiredMixin):

    # def get_success_url(self):
    #     question = get_object_or_404(Question, pk=self.kwargs['pk'])
    #     return reverse_lazy("courses-lesson-detail-view", kwargs={'pk': question.lesson.pk})

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        courses = Course.objects.all()
        subject = get_object_or_404(Subject, slug=course_slug)
        print('SSSSSSSSSSSSSSSSSSSSSS', subject)
        student_ids = Course.objects.get(
            pk=subject.course.id).students.values_list('id', flat=True)
        if request.user.id in list(student_ids):
            course = get_object_or_404(Subject, slug=course_slug)
            print('AAAAAAAAAAAAAAAAA', course)
            lesson = get_object_or_404(Lesson, slug=lesson_slug)
            print('EEEEEEEEEEEEEEEEEEEEEE', lesson)

            context = {'lesson': lesson, 'course': course}
            return render(request, "courses/lesson_detail.html", context)
        else:
            return redirect('courses:suggest')

    # def get_context_data(self, **kwargs):
    #     context = super(LessonDetailView, self).get_context_data(**kwargs)
    #     context["subject"] = Subject.objects.all()
    #     print('***********!!!!!!!!!!!!!!!!!!!!', context)
    #     return context

    # def post(self, request, *args, **kwargs):
    #     for k, v in request.POST.items():
    #         if k != 'csrfmiddlewaretoken':
    #             answer = Answer.objects.filter(question__id=int(
    #                 k.replace('_answers', '')), student=self.request.user).first()
    #             if answer:
    #                 messages.add_message(self.request, messages.ERROR,
    #                                      u'%s асуултанд санал өгсөн байна. Дахин санал өгөх боломжгүй.' % answer.question.text)
    #             else:
    #                 Answer.objects.create(
    #                     question_id=int(k.replace('_answers', '')),
    #                     choice_id=int(v),
    #                     student=request.user,
    #                 )
    #                 answered = True

    # def get_form_kwargs(self):
    #     kwargs = super(LessonDetailView, self).get_form_kwargs()
    #     question = get_object_or_404(Question, pk=self.kwargs['pk'])
    #     kwargs.update({'question': question})
    #     return kwargs

# class AnswerCreate(LoginRequiredMixin, FormView):
#     form_class = QuestionForm

#     def get_success_url(self):
#         question = get_object_or_404(Question, pk=self.kwargs['pk'])
#         return super(AnswerCreate, kwargs={'pk': question.meeting.pk})

#     def get_context_data(self, **kwargs):
#         context = super(AnswerCreate, self).get_context_data(**kwargs)
#         question = get_object_or_404(Question, pk=self.kwargs['pk'])
#         context['question'] = question
#         return context

#     def get_initial(self):
#         initial = super(AnswerCreate, self).get_initial()
#         question = get_object_or_404(Question, pk=self.kwargs['pk'])
#         student = self.request.user
#         if Answer.objects.filter(question=question, student=student).exists():
#             initial['choice'] = Answer.objects.get(
#                 question=question, student=student).choice
#         return initial

#     def get_form_kwargs(self):
#         kwargs = super(AnswerCreate, self).get_form_kwargs()
#         question = get_object_or_404(Question, pk=self.kwargs['pk'])
#         kwargs.update({'question': question})
#         return kwargs

#     def form_valid(self, form):
#         question = get_object_or_404(Question, pk=self.kwargs['pk'])
#         student = self.request.user
#         choice = get_object_or_404(Choice, pk=form.cleaned_data['choice'].id)
#         if Answer.objects.filter(question=question, student=student).exists():
#             form.add_error(None, u"Таны санал өгөх эрх дууссан байна.")
#             return super(AnswerCreate, self).form_invalid(form)
#         Answer.objects.create(
#             question=question,
#             choice=choice,
#             student=student
#         )
#         messages.add_message(self.request, messages.SUCCESS,
#                              u'Санал өгсөн танд баярлалаа.')
#         return super(AnswerCreate, self).form_valid(form)

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
