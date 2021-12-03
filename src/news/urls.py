from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.urls import path

urlpatterns = [
    Nurl("") > "src.website.views.Homepage",
    Nurl("news/") > "src.news.views.NewsList",
    Nurl("news/<slug:slug>/") > "src.news.views.NewsDetail",
    Nurl("news/") > "src.news.views.NewsList",
    Nurl("advice/") > "src.website.views.AdviceNews",
    Nurl("advicedetail/<slug:slug>") > "src.website.views.AdviceDetail",
    Nurl("videonews/") > "src.news.views.VideoNewsList",
    Nurl("videonews/<slug:slug>") > "src.news.views.VideoDetail",
    # Nurl('index/') > 'src.website.views.Index',
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
