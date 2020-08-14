from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    Nurl('') > 'src.website.views.Homepage',
    Nurl('news/') > 'src.news.views.NewsList',
    Nurl('news/<slug:slug>/') > 'src.news.views.NewsDetail',
    Nurl('about/') > 'src.website.views.AboutPage',
    Nurl('news/') > 'src.news.views.NewsList',
    Nurl('special/') > 'src.news.views.SpecialNews',
    Nurl('greetings/') > 'src.website.views.Greetings',
    Nurl('timeline/') > 'src.website.views.TimeLine',
    Nurl('advice/') > 'src.website.views.AdviceNews',

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
