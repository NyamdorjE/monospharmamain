from django.db import models
from django.db.models.fields.files import FileField, ImageField
from django.forms.widgets import Media
from django.utils.text import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Testimonail(models.Model):
    content = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    profile = models.FileField(upload_to="media/testimonails/profile")
    person = models.CharField(max_length=55, verbose_name=_("Guest"))
    job = models.CharField(max_length=128, verbose_name=_("Guest job"), default="")

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonial")

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
        verbose_name = _("Advice title")
        verbose_name_plural = _("Advice title")
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Advice(models.Model):
    category = models.ForeignKey(AdviceCategory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = models.SlugField()
    content = RichTextField(blank=True, null=True, verbose_name=_("content"))
    author = models.CharField(verbose_name=_("Author"), max_length=128)
    photo = models.ImageField(upload_to="advice_image", null=True, blank=True)
    created_on = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Advice")
        verbose_name_plural = _("Advice")
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Partner(models.Model):
    image = models.FileField(
        verbose_name=_("Хамтрагч байгуулгын зураг"), upload_to="media/partner"
    )
    position = models.IntegerField()

    class Meta:
        verbose_name = _("Хамтрагч байгуулгын зураг")
        verbose_name = _("Хамтрагч байгуулгын зураг")
        ordering = ["-position"]


class LeftFeaturedProduct(models.Model):

    link_to_emonos = models.CharField(max_length=255)
    picture = models.FileField(upload_to="media/Featuredproduct/")

    class Meta:
        verbose_name = _("Зүүн танилцуулга бүтээгдэхүүн")
        ordering = ["link_to_emonos"]


class RightFeaturedProduct(models.Model):

    link_to_emonos = models.CharField(max_length=255)
    picture = models.FileField(upload_to="media/Featuredproduct/")

    class Meta:
        verbose_name = _("Баруун танилцуулга бүтээгдэхүүн")
        ordering = ["link_to_emonos"]


class Gallery(models.Model):
    title = models.CharField(
        max_length=255, verbose_name=_("Гарчиг хэсэг"), null=True, blank=True
    )
    description = models.CharField(
        max_length=255, verbose_name=_("Тайлбар хэсэг"), null=True, blank=True
    )
    image = models.FileField(upload_to="media/gallery")

    class Meta:
        verbose_name = _("Зургын сан")
        ordering = ["title"]

    # def __str__(self):
    #     return self.title


class Counter(models.Model):
    number = models.IntegerField(verbose_name=_("Тоолуур гүйх тоонууд"))
    content = models.CharField(max_length=255, verbose_name=_("Тоон доор орох тайлбар"))
    position = models.IntegerField()
    picture = models.FileField(upload_to="media/counter")

    class Meta:
        verbose_name = _("Тоолуур")
        ordering = ["position"]


class Banner(models.Model):
    alt_text = models.CharField(
        max_length=550,
        verbose_name=_("Баннер зурагын хайлтын системд туслах тэскт"),
        null=True,
    )
    photo = models.FileField(
        upload_to="media/banners", verbose_name=_("Баннер зураг орох")
    )
    position = models.IntegerField()

    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name = _("Banner picture")
        ordering = ["position"]


class BannerAboutUs(models.Model):
    alt_text = models.CharField(
        max_length=550,
        verbose_name=_("Баннер зурагын хайлтын системд туслах тэскт"),
        null=True,
    )
    photo = models.FileField(
        upload_to="media/banners", verbose_name=_("Баннер зураг орох")
    )
    position = models.IntegerField()

    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name = _("Бидний тухай хуудас баннер")
        ordering = ["position"]


class BannerVideo(models.Model):
    src = models.CharField(max_length=255, verbose_name=_("Banner video"))


class Counter(models.Model):
    background = ImageField(
        upload_to="counter", verbose_name=_("Арын зураг"), null=True, blank=True
    )
    title = models.CharField(verbose_name=_("Гарчиг"), max_length=255)
    icon = models.CharField(
        verbose_name=_("Icon бичнэ"),
        max_length=55,
        help_text="icon-check-mark, гэх мэт icon-ууд оруулж өгнө",
        null=True,
        blank=True,
    )
    number = models.CharField(
        verbose_name=_("Тоо тоолуур"),
        max_length=55,
        help_text="250сая гэсэн байдлаар тоог оруулна",
    )
    order = models.IntegerField(
        verbose_name=_("Байрших байрлал"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Тоолуур")
        verbose_name_plural = _("Тоолуур")
        ordering = ["number"]

    def __str__(self):
        return self.title


class Introduction(models.Model):
    context = RichTextUploadingField(verbose_name=_("Танилцуулга"))

    class Meta:
        verbose_name = _("Компаны танилцуулга")
        verbose_name_plural = _("Компаны танилцуулга")


class Mission(models.Model):
    context = RichTextUploadingField(verbose_name=_("Эрхэм зорилго"))

    class Meta:
        verbose_name = _("Эрхэм зорилго")
        verbose_name_plural = _("Эрхэм зорилго")


class DirectorsGreetings(models.Model):
    image = models.FileField(
        upload_to="media/zahiral", verbose_name=_("Захиралын зураг")
    )
    context = RichTextUploadingField(verbose_name=_("Контэнт"))

    class Meta:
        verbose_name = _("Захиралын мэндчилгээ")
        verbose_name_plural = _("Захиралын мэндчилгээ")


class AboutUsCards(models.Model):
    image = models.FileField(upload_to="media/featurebox", verbose_name=_("Зураг"))
    title = models.CharField(verbose_name=_("Гарчиг"), max_length=500)
    link = models.CharField(
        verbose_name=_("Үсрэх линк"), max_length=500, null=True, blank=True
    )
    context = models.TextField(verbose_name=_("Контэнт"))

    class Meta:
        verbose_name = _("Бидний тухай хэсэгын карт")
        verbose_name_plural = _("Бидний тухай хэсэгын карт")


class HrBanner(models.Model):
    alt_text = models.CharField(
        max_length=550,
        verbose_name=_("Баннер зурагын хайлтын системд туслах тэскт"),
        null=True,
    )
    photo = models.FileField(
        upload_to="media/hrbanner", verbose_name=_("Баннер зураг орох")
    )
    position = models.IntegerField()

    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name = _("HR хуудас баннер")
        ordering = ["position"]
