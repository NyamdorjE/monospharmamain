"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from src.base.urls import Nurl
from .views import DetailView, PollTake


from src.poll import views

urlpatterns = [
    path('poll/', views.home, name='home'),
    # path('polldetail/<slug:slug>', views.detail, name='detail'),
    Nurl('poll/<slug:slug>/') > 'src.poll.views.DetailView',
    # url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
    #     view=PollTake.as_view(),
    #     name='quiz_question'),
]
