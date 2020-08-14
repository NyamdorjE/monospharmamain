from django.shortcuts import render
from .models import ProductCategory, Product
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


class ProductList(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'product/product.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['product'] = self.get_queryset()
        context['category'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        search_text = self.request.GET.get('search_text', None)
        cat_id = self.request.GET.get('cat_id')
        if search_text:
            queryset = queryset.filter(
                Q(name__icontains=search_text) |
                Q(suggest__icontains=search_text)
            )
            return queryset

        else:
            product_list = Product.objects.filter(categories__id=cat_id)
            product = Product.objects.all()

        if product_list:
            return product_list
        else:
            return product
