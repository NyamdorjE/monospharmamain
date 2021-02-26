from django.urls import path
from django.conf.urls import url
from src.base.urls import Nurl

from .views import (
    LessonQuizView,
    QuizMarkingList,
    QuizDetailView,
    QuizMarkingDetail,
    QuizUserProgressView,
    QuizTake,
)


urlpatterns = [
    # path('courses/<course_slug>/<lesson_slug>/<quiz_url>',
    #      (LessonQuizView.as_view()), name='lesson_detail_quiz'),
    # path('courses/<course_slug>/<lesson_slug>/<quiz_url>',
    #      (LessonQuizView.as_view()), name='lesson_detail_quiz'),
    # url(regex=r'^course/(?P<course_slug>[^/]+)/(?P<lesson_slug>[^/]+)/(?P<quiz_url>[-\w]+)$',
    #     view=LessonQuizView.as_view(),
    #     name='lesson_detail_quiz'),
    # url(r'(?P<lesson_id>[^/]+)/(?P<quiz_id>[-\w]+)$',
    #     LessonQuizView.as_view()),
    # url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
    #     view=QuizTake.as_view(),
    #     name='quiz_question'),
    # url(regex=r'^quizzes/$',
    #     view=LessonQuizView.as_view(),
    #     name='lesson_detail_quiz'),
    # url(regex=r'^quizzes/$',
    #     view=LessonQuizView.as_view(),
    #     name='quiz_index'),
    # url(regex=r"^marking/$", view=QuizMarkingList.as_view(), name="quiz_marking"),
    # url(
    #     regex=r"^marking/(?P<pk>[\d.]+)/$",
    #     view=QuizMarkingDetail.as_view(),
    #     name="quiz_marking_detail",
    # ),
    # url(
    #     regex=r"^lesson(?P<slug>[\w-]+)/$",
    #     view=LessonQuizView.as_view(),
    #     name="quiz_start_page",
    # ),
    # url(
    #     regex=r"^lesson(?P<slug>[\w-]+)/(?P<quiz_name>[\w-]+)/take/$",
    #     view=QuizTake.as_view(),
    #     name="quiz_question",
    # ),


    url(regex=r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(regex=r'^marking/$',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    url(regex=r'^marking/(?P<pk>[\d.]+)/$',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),


    url(regex=r'^lesson(?P<slug>[\w-]+)/$',
        view=LessonQuizView.as_view(),
        name='quiz_start_page'),

    url(regex=r'^(?P<slug>[\w-]+)/(?P<quiz_name>[\w-]+)/take/$',
        view=QuizTake.as_view(),
        name='quiz_question'),
]
