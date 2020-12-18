from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    Nurl('about/') > 'src.website.views.About',
    Nurl("360_virtual/") > 'src.website.views.Virtual',



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
