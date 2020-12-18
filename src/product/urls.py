from src.base.urls import Nurl
from django.urls import include, path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from .fetch import product_fetch

urlpatterns = [
    Nurl("product/") > "src.product.views.ProductList",
    Nurl("product/<pk>") > "src.product.views.ProductDetailView",
    Nurl("productalph") > "src.product.views.ProductAlphabet",
    path("fetch/product/", product_fetch),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
