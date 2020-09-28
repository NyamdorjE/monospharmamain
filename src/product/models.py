from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField
# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    category_type = (
        ("энгийн", "Энгийн"),
    )
    cate_type = models.CharField(
        max_length=255, choices=category_type, default="энгийн")

    class Meta:
        verbose_name = _('Product category')
        verbose_name_plural = _('Prodcut categories ')
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_products(self):
        return Product.objects.filter(category=self)


# class Classification(models.Model):
#     classification_name = models.CharField(
#         max_length=255, verbose_name=_('Classification type'))

#     class Meta:
#         verbose_name = _('Classification')
#         ordering = ['classification_name']

#     def __str__(self):
#         return self.classification_name


class Type(models.Model):
    type_name = models.CharField(
        max_length=255, verbose_name=_('Type of product'))

    class Meta:
        verbose_name = _('Type of product')
        ordering = ['type_name']

    def __str__(self):
        return self.type_name


class ProductForm(models.Model):
    form_name = models.CharField(
        max_length=255, verbose_name=_('ProductForm '))

    class Meta:
        verbose_name = _('ProductForm')
        ordering = ['form_name']

    def __str__(self):
        return self.form_name


class Product(models.Model):
    categories = models.ForeignKey(ProductCategory, verbose_name=_(
        "Category"), on_delete=models.CASCADE, related_name="Product")
    product_id = models.IntegerField(
        verbose_name=_("Product id"), primary_key=True)
    # classification = models.ForeignKey("Classification", verbose_name=_(
    #     "Classification"), on_delete=models.CASCADE, null=True, blank=True)
    producttype = models.ForeignKey("Type", verbose_name=_(
        "producttype"), on_delete=models.CASCADE)
    productForm = models.ForeignKey("ProductForm", verbose_name=_(
        "ProductForm"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_(
        "Product name "), max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name=_('Product Slug'), unique=True)
    international_name = models.CharField(
        max_length=255, verbose_name=_('Product intertational name'))
    ingredients = models.CharField(verbose_name=_(
        "Product ingredients"), max_length=500)
    suggest = models.CharField(max_length=1000, verbose_name=_('How to use '))
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created on'))
    image = models.ImageField(verbose_name=_(
        'Picture'), upload_to='media/product/image/')

    is_product_new = models.BooleanField(default=False)
    link = models.CharField(verbose_name=_(
        'Link to emonos'), max_length=355, null=True)
    daatgal = models.BooleanField(
        default=False, help_text="Бүтээгдэхүүн даатгалд хамрагддаг бол зөв болгоно уу")
    jor = models.BooleanField(
        default=False, help_text="Бүтээгдэхүүн жортой бол зөвлөн үү")

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Prodcuts')
        ordering = ['name']

    @property
    def get_products(self):
        return Products.objects.filter(categories__name=self.title)

    def __str__(self):
        return self.name
