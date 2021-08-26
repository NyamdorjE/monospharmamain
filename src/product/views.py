from django.http import request

from .models import ProductCategory, Product, ProductCategoryImage
from django.views import generic
from django.db.models import Q
from django.views.generic import ListView
from django.utils.translation import gettext as _


class ProductList(ListView):
    paginate_by = 100
    queryset = Product.objects.all()
    template_name = "product/product.html"

    def get_context_data(self, **kwargs):
        a = self.request.GET.get("cat_id")
        print(a)
        context = super(ProductList, self).get_context_data(**kwargs)
        context["product"] = self.get_queryset()
        context["category"] = ProductCategory.objects.all()
        context["cat"] = ProductCategoryImage.objects.filter(
            id=self.request.GET.get("cat_id")
        )
        context["newproduct"] = Product.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        cat_id = self.request.GET.get("cat_id")
        if search_text:
            queryset = queryset.filter(
                Q(name__icontains=search_text)
                | Q(instructions__icontains=search_text)
                | Q(ingredients__icontains=search_text)
                | Q(warnings__icontains=search_text)
                | Q(description__icontains=search_text)
            )
            return queryset

        if cat_id:
            product_list = Product.objects.filter(category=cat_id)
            return product_list
        else:
            product = Product.objects.all()
            return product


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'product/productdetail.html'
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['product'] = News.objects.all()


#         return context
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/productdetail.html"


class ProductAlphabet(generic.ListView):
    queryset = Product.objects.order_by("name")
    template_name = "product/productalphabet.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductAlphabet, self).get_context_data(**kwargs)
        context["product"] = self.get_queryset()
        context["category"] = ProductCategory.objects.all()
        context["newproduct"] = Product.objects.order_by("name")
        return context

    def get_queryset(self):
        queryset = super(ProductAlphabet, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        cat_id = self.request.GET.get("cat_id")
        if search_text:
            queryset = queryset.filter(
                Q(name__icontains=search_text) | Q(suggest__icontains=search_text)
            )
            return queryset

        else:
            product_list = Product.objects.filter(web_category=cat_id)
            product = Product.objects.all()

        if product_list:
            return product_list
        else:
            return product


class ProductCategoryList(ListView):
    paginate_by = 12
    queryset = Product.objects.all()
    template_name = "product/productcat.html"

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryList, self).get_context_data(**kwargs)
        context["product"] = self.get_queryset()
        context["category"] = ProductCategory.objects.all()
        context["cat"] = ProductCategoryImage.objects.all()
        context["newproduct"] = Product.objects.all()
        return context
