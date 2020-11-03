from django.db import models
from django.forms.widgets import Media
from django.utils.text import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class Testimonail(models.Model):
    content = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    profile = models.FileField(upload_to="media/testimonails/profile")
    person = models.CharField(max_length=55, verbose_name=_("Author"))
    job = models.CharField(max_length=128, verbose_name=_("Job"), default="")

    class Meta:
        verbose_name = _("Үйлвэртэй танилцсан сэтгэгдэл")
        verbose_name_plural = _("Үйлвэртэй танилцсан сэтгэгдэл")

    def __str__(self):
        return self.person


# class Gallery(models.Model):
#     title = models.CharField(max_length=255, verbose_name=_('Title'))
#     picture = models.FileField(upload_to="media/gallery/")

#     class Meta:
#         verbose_name = _('Gallery')
#         ordering = ['title']

#     def __str__(self):
#         return self.title


class AdviceCategory(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=100,
    )

    class Meta:
        verbose_name = _("Зөвөлгөөний ангиллал")
        verbose_name_plural = _("Зөвөлгөөний ангиллал")
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Advice(models.Model):
    category = models.ForeignKey(AdviceCategory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    slug = models.SlugField()
    content = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    author = models.CharField(verbose_name=_("Author"), max_length=128)
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Зөвлөгөө")
        verbose_name_plural = _("Зөвлөгөө")
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.FileField(verbose_name=_("Image"), upload_to="media/partner")
    position = models.IntegerField()

    class Meta:
        verbose_name = _("Хамтрагч байгуулгын зураг")
        verbose_name = _("Хамтрагч байгуулгын зураг")
        ordering = ["-position"]


class FeaturedProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ad = models.CharField(max_length=255)
    emonos = models.CharField(max_length=255)
    picture = models.FileField(upload_to="media/Featuredproduct/")

    class Meta:
        verbose_name = _("Танилцуулга бүтээгдэхүүн")
        ordering = ["title"]

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(
        max_length=255, verbose_name=_("Gallery"), null=True, blank=True
    )
    description = models.CharField(
        max_length=255, verbose_name=_("Description"), null=True, blank=True
    )
    image = models.FileField(upload_to="media/gallery")

    class Meta:
        verbose_name = _("Зурагын сан")
        ordering = ["title"]

    # def __str__(self):
    #     return self.title


class Counter(models.Model):
    number = models.IntegerField(verbose_name=_("Counter number"))
    content = models.CharField(
        max_length=255, verbose_name=_("Counter number description")
    )
    position = models.IntegerField()
    picture = models.FileField(upload_to="media/counter")

    class Meta:
        verbose_name = _("Тоолуур")
        ordering = ["position"]


class Banner(models.Model):
    alt_text = models.CharField(max_length=550, verbose_name=_("Banner"), null=True)
    photo = models.FileField(upload_to="media/banners", verbose_name=_("Banner photo"))
    position = models.IntegerField()

    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name = _("Баннер зураг")
        ordering = ["position"]


class BannerVideo(models.Model):
    src = models.CharField(max_length=255, verbose_name=_("Баннер бичлэг"))
