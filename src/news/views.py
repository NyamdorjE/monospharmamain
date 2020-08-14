from django.shortcuts import render
from src.news.models import Category, News
from src.courses.models import Course
from src.website.models import Advice
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


# Create your views here.


class NewsList(generic.ListView):
    queryset = News.objects.all()
    template_name = 'news/news.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()
        return context

    def get_queryset(self):
        queryset = super(NewsList, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset


class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['News_list'] = News.objects.all()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()

        return context


class SpecialNews(generic.ListView):
    queryset = News.objects.filter(is_special='True')
    template_name = 'news/specialnews.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(SpecialNews, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['search_text'] = self.request.GET.get('search_text', '')
        context['category'] = Course.objects.all()
        return context

    def get_queryset(self):
        queryset = super(SpecialNews, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset
