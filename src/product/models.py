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
        ("зүрх судас", "Зүрх судас"),
        ("витамин", "Витамин"),
        ("хүүхэд", "Хүүхэд")
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


class Product(models.Model):
    categories = models.ForeignKey(ProductCategory, verbose_name=_(
        "Category"), on_delete=models.CASCADE, related_name="Product")
    product_id = models.IntegerField(
        verbose_name=_("Product id"), primary_key=True)
    name = models.CharField(verbose_name=_(
        "Product name "), max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name=_('Product Slug'), unique=True)
    ingredients = models.CharField(verbose_name=_(
        "Product ingredients"), max_length=500)
    suggest = models.CharField(max_length=1000, verbose_name=_('How to use '))
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created on'))
    image = models.ImageField(verbose_name=_(
        'Picture'), upload_to='media/product/image/')
    price = models.CharField(
        max_length=150, verbose_name=_('Price'),  default="₮")
    is_product_new = models.BooleanField(default=False)
    link = models.CharField(verbose_name=_(
        'Link to emonos'), max_length=355, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Prodcuts')
        ordering = ['created_on']

    @property
    def get_products(self):
        return Products.objects.filter(categories__name=self.title)

    def __str__(self):
        return self.name
