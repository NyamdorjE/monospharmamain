from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField

# Create your models here.


class ProductCategory(models.Model):
    parent = models.ForeignKey(
        "self",
        to_field="id",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="parent_id",
        verbose_name="Толгой ангилал",
        related_name="categories",
    )
    name = models.CharField(max_length=200, verbose_name="Нэр", null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created on"), null=True, blank=True
    )

    class Meta:
        ordering = ["created_at", "id"]
        verbose_name = "Бүтээгдэхүүний ангилал"
        verbose_name_plural = "Бүтээгдэхүүний ангилал"

    def __str__(self):
        return self.name


# class Classification(models.Model):
#     classification_name = models.CharField(
#         max_length=255, verbose_name=_('Classification type'))

#     class Meta:
#         verbose_name = _('Classification')
#         ordering = ['classification_name']

#     def __str__(self):
#         return self.classification_name


class Type(models.Model):
    type_name = models.CharField(max_length=255, verbose_name=_("Type of product"))

    class Meta:
        verbose_name = _("Бүтээгдэхүүний төрөл")
        ordering = ["type_name"]

    def __str__(self):
        return self.type_name


class ProductForm(models.Model):
    form_name = models.CharField(max_length=255, verbose_name=_("ProductForm "))

    class Meta:
        verbose_name = _("Бүтээгдэхүүний хэлбэр")
        ordering = ["form_name"]

    def __str__(self):
        return self.form_name


class Product(models.Model):
    web_category = models.ForeignKey(
        "product.productCategory",
        verbose_name="Ангилал",
        to_field="id",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="web_category_id",
        related_name="products",
    )
    product_id = models.IntegerField(
        verbose_name=_("Бүтээгдэхүүн дотоод код"),
        null=True,
        blank=True,
    )
    # classification = models.ForeignKey("Classification", verbose_name=_(
    #     "Classification"), on_delete=models.CASCADE, null=True, blank=True)
    producttype = models.ForeignKey(
        "Type",
        verbose_name=_("producttype"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    productForm = models.ForeignKey(
        "ProductForm",
        verbose_name=_("ProductForm"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_("Product name "),
        max_length=255,
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Product Slug"),
        null=True,
        blank=True,
    )
    description = RichTextField(null=True, blank=True)
    instructions = RichTextField(null=True, blank=True)

    ingredients = RichTextField(null=True, blank=True)
    warnings = RichTextField(null=True, blank=True)
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created on"), null=True, blank=True
    )
    photo = models.ImageField(
        verbose_name=_("Picture"),
        upload_to="media/product/image/",
        null=True,
        blank=True,
    )

    is_product_new = models.BooleanField(default=False, null=True, blank=True)
    international_name = models.CharField(
        max_length=255,
        verbose_name=_("Product intertational name"),
        null=True,
        blank=True,
    )
    link = models.CharField(
        verbose_name=_("Link to emonos"), max_length=355, null=True, blank=True
    )
    daatgal = models.BooleanField(
        default=False,
        help_text="Бүтээгдэхүүн даатгалд хамрагддаг бол зөв болгоно уу",
        null=True,
        blank=True,
    )
    jor = models.BooleanField(
        default=False,
        help_text="Бүтээгдэхүүн жортой бол зөвлөн үү",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Бүтээгдэхүүн")
        verbose_name_plural = _("Бүтээгдэхүүн")
        ordering = ["name"]

    # @property
    # def get_products(self):
    #     return Products.objects.filter(categories__name=self.title)

    def __str__(self):
        return self.name
