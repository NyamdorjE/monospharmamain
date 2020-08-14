from django.urls import path
from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.decorators import login_required

from src.courses.views import HomeView, AboutView, CourseListView, CourseDetailView, LessonDetailView, SearchView, SuggestView
app_name = 'courses'

urlpatterns = [
    path('course/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('suggest/', SuggestView.as_view(), name='suggest'),
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()),
         name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/',
         login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='search_course'),




]
