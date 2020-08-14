from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    category_type = (
        ("news", "News"),
        ("research", "Research")

    )
    cate_type = models.CharField(
        max_length=255, choices=category_type, default="news")

    class Meta:
        verbose_name = _("Мэдээ ангиллал")
        verbose_name_plural = _("Мэдээ ангиллал")
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_products(self):
        return News.objects.filter(category=self)


class News(models.Model):
    category = models.ForeignKey(Category, verbose_name=_(
        'Category'), on_delete=models.CASCADE, related_name="News")
    title = models.CharField(
        max_length=255, verbose_name=_('Title'), unique=True)
    slug = models.SlugField(
        max_length=255, verbose_name=_('News Slug'), unique=True)
    author = models.CharField(max_length=255, verbose_name=_('Created by'))
    content = RichTextField(blank=True, null=True, verbose_name=_('Content'))
    image = models.ImageField(verbose_name=(
        'Picture'), upload_to='media/news/')
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created on'))
    updated_on = models.DateTimeField(
        auto_now=True,  verbose_name=_('Updated on'))
    is_special = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['-created_on']

    def __str__(self):
        return self.title
