"""monospharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url

from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from src.base.models import humanresource, contact
from src.base.models.humanresource import EmailAttachementView
from src.accounts import views as user_views
from src.courses import views as courses_views
from src.news import views as news_views
from src.base.urls import Nurl


app_name = "polls"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("humanresource/", humanresource.hrview, name="humanresource"),
    # path('humanresource/<slug>', HrDetailView.as_view(), name='humandetailview'),
    # Nurl('humanresource/<slug:slug>/') > 'src.base.models.humanresource.HrDetailView',
    path(
        "humanresource/<slug:slug>/",
        EmailAttachementView.as_view(),
        name="humandetailview",
    ),
    path("contact/", contact.contact, name="contact"),
    path("ckeditor", include("ckeditor_uploader.urls")),
    # path('contact/', contact.contact, name='contact'),
    # path('contact/', contact.contactview, name='contact'),
    # path('contact/', EmailAttachementView.as_view(), name='emailattachment'),
    path("", include("src.accounts.urls")),
    path("", include("src.courses.urls")),
    path("", include("src.news.urls")),
    path("", include("src.product.urls")),
    path("", include("src.poll.urls")),
    path("", include("src.quiz.urls")),
    path("", include("src.website.urls")),
    url(r"^accounts/", include("registration.backends.default.urls")),
    url(r"^i18n/", include("django.conf.urls.i18n")),
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    # url(r'^contact/', include('contact.urls', namespace='contact')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
