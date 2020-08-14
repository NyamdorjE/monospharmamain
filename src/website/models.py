from django.db import models
from django.utils.text import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class Testimonail(models.Model):
    content = RichTextField(blank=True, null=True, verbose_name=_('Content'))
    profile = models.FileField(upload_to="media/testimonails/profile")
    person = models.CharField(max_length=55, verbose_name=_('Author'))
    job = models.CharField(max_length=128, verbose_name=_('Job'), default='')

    class Meta:
        verbose_name = _('Testimonail')
        verbose_name_plural = _('Testimonails')

    def __str__(self):
        return self.person


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    picture = models.FileField(upload_to="media/gallery/")

    class Meta:
        verbose_name = _('Gallery')
        ordering = ['title']

    def __str__(self):
        return self.title


class AdviceCategory(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100,)

    class Meta:
        verbose_name = _('Advice category')
        verbose_name_plural = _('Advice categories')
        ordering = ['-title']

    def __str__(self):
        return self.title


class Advice(models.Model):
    category = models.ForeignKey(AdviceCategory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    content = RichTextField(blank=True, null=True, verbose_name=_('Content'))
    author = models.CharField(verbose_name=_('Author'), max_length=128)
    created_on = models.DateTimeField(
        verbose_name=_('Created on'), auto_now_add=True,)

    class Meta:
        verbose_name = _('Advice')
        verbose_name_plural = _('Advices')
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.FileField(verbose_name=_(
        'Image'), upload_to="media/partner")
    position = models.IntegerField()

    class Meta:
        verbose_name = _('Partner')
        verbose_name = _('Partners')
        ordering = ['-position']
