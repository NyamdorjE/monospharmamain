from django.shortcuts import render
from django.template import context
from src.news.models import Category, News, VideoNews, VideoNewsCategory
from src.courses.models import Course
from src.website.models import Advice
from src.product.models import Product
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
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()
        # context['newproduct'] = Product.objects.filter(is_product_new=True)

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


class ProductNews(generic.ListView):
    queryset = News.objects.filter(category='2')
    template_name = 'news/productnews.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductNews, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()
        # context['newproduct'] = Product.objects.filter(is_product_new=True)

        return context

    def get_queryset(self):
        queryset = super(ProductNews, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset


class OurParticipation(generic.ListView):
    queryset = News.objects.filter(category='1')
    template_name = 'news/Ourpart.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(OurParticipation, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()
        # context['newproduct'] = Product.objects.filter(is_product_new=True)

        return context

    def get_queryset(self):
        queryset = super(OurParticipation, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset


class OurParticipation(generic.ListView):
    queryset = News.objects.filter(category='3')
    template_name = 'news/Ourpart.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(OurParticipation, self).get_context_data(**kwargs)
        context['news'] = self.get_queryset()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()
        # context['newproduct'] = Product.objects.filter(is_product_new=True)

        return context

    def get_queryset(self):
        queryset = super(OurParticipation, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) |
                Q(content__icontains=search_text)
            )
        return queryset


# def videos(request):
#     videos = Videos.objects.filter(video_type=1)
#     return render('news/video.html', locals(), context_instance=RequestContext(request))


# def casting(request):
#     videos = Videos.objects.filter(video_type=2)
#     return render('news/casting.html', locals(), context_instance=RequestContext(request))

class VideoNewsList(generic.ListView):
    queryset = VideoNews.objects.all()
    template_name = 'news/video.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(VideoNewsList, self).get_context_data(**kwargs)
        context['video'] = VideoNews.objects.all()
        context['special'] = News.objects.filter(is_special='True')
        context['category_list'] = Category.objects.filter(cate_type="news")
        context['category'] = Course.objects.all()
        context['advice'] = Advice.objects.all()

        return context

    def get_queryset(self):
        queryset = super(VideoNewsList, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text)
            )
        return queryset
