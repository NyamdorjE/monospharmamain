from src.news.models import Category, News, VideoNews
from src.courses.models import Course
from src.website.models import Advice
from django.views.generic import ListView
from django.views import generic
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponseRedirect

from django.utils.translation import gettext as _


# Create your views here.


class NewsList(ListView):
    queryset = News.objects.all()
    template_name = "news/news.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context["news"] = self.get_queryset()
        context["latest"] = Advice.objects.all()
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()
        context["advice"] = Advice.objects.all()
        # context['newproduct'] = Product.objects.filter(is_product_new=True)

        return context

    def get_queryset(self):
        queryset = super(NewsList, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        news_id = self.request.GET.get("news_id")
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
            return queryset
        if news_id:
            news_list = News.objects.filter(category=news_id)
            return news_list
        else:
            return News.objects.all()


class NewsDetail(generic.DetailView):
    model = News
    template_name = "news/news_detail.html"

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context["News_list"] = News.objects.all()
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()

        return context


class VideoNewsList(generic.ListView):
    queryset = VideoNews.objects.all()
    template_name = "news/video.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(VideoNewsList, self).get_context_data(**kwargs)
        context["video"] = VideoNews.objects.all()
        context["special"] = News.objects.filter(is_special="True")
        context["latest"] = News.objects.all()
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()
        context["advice"] = Advice.objects.all()

        return context

    def get_queryset(self):
        queryset = super(VideoNewsList, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(Q(title__icontains=search_text))
        return queryset


class VideoDetail(generic.DetailView):
    model = VideoNews
    template_name = "news/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VideoDetail, self).get_context_data(**kwargs)
        context["video"] = VideoNews.objects.all()

        return context


def change_language(request):
    response = HttpResponseRedirect("/")
    if request.method == "POST":
        language = request.POST.get("language")
        if language:
            if language != settings.LANGUAGE_CODE and [
                lang for lang in settings.LANGUAGES if lang[0] == language
            ]:
                redirect_path = f"/{language}/"
            elif language == settings.LANGUAGE_CODE:
                redirect_path = "/"
            else:
                return response
            from django.utils import translation

            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
