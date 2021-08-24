from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    Nurl("about/") > "src.website.views.About",
    Nurl("360_virtual/") > "src.website.views.Virtual",
    Nurl("aboutus/") > "src.website.views.AboutUs",
    Nurl("taniltsuulga/") > "src.website.views.Taniltsuulga",
    Nurl("zahiral/") > "src.website.views.Zahiral",
    Nurl("timeline/") > "src.website.views.Timeline",
    Nurl("vision/") > "src.website.views.Vision",
    Nurl("amjilt/") > "src.website.views.Amjilt",
    Nurl("hrnew/") > "src.website.views.HrNew",
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
