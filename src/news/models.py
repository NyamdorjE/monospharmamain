from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    category_type = (
        ("news", "News"),

    )
    cate_type = models.CharField(
        max_length=255, choices=category_type, default="news")

    class Meta:
        verbose_name = _("News category")
        verbose_name_plural = _("News category")
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
    author = models.CharField(
        max_length=255, verbose_name=_('Created by'), default="Админ")
    content = RichTextUploadingField(
        blank=True, null=True, verbose_name=_('Content'))
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


class VideoNewsCategory(models.Model):
    category_name = models.CharField(
        max_length=255, verbose_name=_('Video news category'))

    class Meta:
        verbose_name = _('Video news category')
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class VideoNews(models.Model):
    category = models.ForeignKey(VideoNewsCategory, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255, verbose_name=_("Video news title"))
    video = models.FileField(
        upload_to="media/videonews", null=True, blank=True)
    youtube_url = models.CharField(
        max_length=500, verbose_name=_('Youtube video embed url'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Video news")
        ordering = ["created_at"]
