from django.shortcuts import render
from src.news.models import Category, News
from src.courses.models import Course
from src.product.models import Product, ProductCategory
from django.template import RequestContext


from .models import (
    AboutUsCards,
    Advice,
    AdviceCategory,
    BannerAboutUs,
    HrBanner,
    HrCard,
    HrContent,
    Taniltsuulga,
    Testimonail,
    Gallery,
    LeftFeaturedProduct,
    RightFeaturedProduct,
    BannerVideo,
    Banner,
)
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


class Homepage(generic.ListView):
    queryset = News.objects.all().order_by("created_on")
    template_name = "news/homepage.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context["special"] = News.objects.filter(is_special="True")
        context["category"] = Course.objects.all()
        context["news"] = News.objects.all().order_by("-created_on")
        context["newproduct"] = Product.objects.filter(is_product_new=True)
        context["advice"] = Advice.objects.all()
        context["testimonail"] = Testimonail.objects.all()
        context["leftfeatured"] = LeftFeaturedProduct.objects.all()
        context["rigthfeatured"] = LeftFeaturedProduct.objects.all()
        context["banner"] = Banner.objects.all()
        context["bannervideo"] = BannerVideo.objects.all()
        return context


class About(TemplateView):
    template_name = "website/about.html"
    queryset = News.objects.all().order_by("created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context["special"] = News.objects.filter(is_special="True")
        context["category"] = Course.objects.all()
        context["news"] = News.objects.all().order_by("-created_on")

        return context


class AboutUs(TemplateView):
    template_name = "website/aboutus.html"
    queryset = AboutUsCards.objects.all()
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context["banner"] = BannerAboutUs.objects.all()
        context["queryset"] = AboutUsCards.objects.all()
        return context


class Vision(TemplateView):
    template_name = "website/vision.html"


class Amjilt(TemplateView):
    template_name = "website/amjilt.html"


class Emsudlal(TemplateView):
    template_name = "website/emsudlal.html"


class TaniltsuulgaView(TemplateView):
    template_name = "website/taniltsuulga.html"
    queryset = News.objects.all().order_by("created_on")

    def get_context_data(self, **kwargs):
        context = super(TaniltsuulgaView, self).get_context_data(**kwargs)
        context["object"] = Taniltsuulga.objects.all()

        return context


class Zahiral(TemplateView):
    template_name = "website/zahiral.html"
    queryset = News.objects.all().order_by("created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(Zahiral, self).get_context_data(**kwargs)
        context["special"] = News.objects.filter(is_special="True")
        context["category"] = Course.objects.all()
        context["banner"] = BannerAboutUs.objects.all()
        context["news"] = News.objects.all().order_by("-created_on")

        return context


class Timeline(TemplateView):
    template_name = "website/timeline.html"
    queryset = News.objects.all().order_by("created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(Timeline, self).get_context_data(**kwargs)
        context["special"] = News.objects.filter(is_special="True")
        context["category"] = Course.objects.all()
        context["banner"] = BannerAboutUs.objects.all()
        context["news"] = News.objects.all().order_by("-created_on")

        return context


class AdviceNews(generic.ListView):
    queryset = Advice.objects.all()
    template_name = "news/advice.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(AdviceNews, self).get_context_data(**kwargs)
        context["news"] = News.objects.all().order_by("-created_on")
        context["advice"] = self.get_queryset()
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["search_text"] = self.request.GET.get("search_text", "")

        return context

    def get_queryset(self):
        queryset = super(AdviceNews, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset


class AdviceDetail(generic.DetailView):
    model = Advice
    template_name = "news/advicedetail.html"

    def get_context_data(self, **kwargs):
        context = super(AdviceDetail, self).get_context_data(**kwargs)
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()

        return context


class Virtual(TemplateView):
    template_name = "virtual_tour/index.html"


class HrNew(TemplateView):
    template_name = "website/hrnew.html"
    queryset = News.objects.all().order_by("created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HrNew, self).get_context_data(**kwargs)
        context["banner"] = HrBanner.objects.all()
        context["object"] = HrContent.objects.all().order_by("position")
        context["card"] = HrCard.objects.all().order_by("position")

        return context
