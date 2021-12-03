from ckeditor import fields
from modeltranslation.translator import translator, TranslationOptions
from src.news.models import News, Category, VideoNews
from src.product.models import Product, ProductCategory, ProductForm, Type
from src.website.models import (
    Testimonail,
    AdviceCategory,
    Advice,
    AboutUsCards,
    Partner,
    Banner,
    BannerAboutUs,
    BannerVideo,
    Counter,
    Introduction,
    Mission,
    DirectorsGreetings,
    HrCard,
    HrBanner,
    HrContent,
    Taniltsuulga,
)


class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content")


translator.register(News, NewsTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Category, CategoryTranslationOptions)


class VideoNewsTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(VideoNews, VideoNewsTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
        "instructions",
        "ingredients",
        "warnings",
        "international_name",
    )


translator.register(Product, ProductTranslationOptions)


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(ProductCategory, ProductCategoryTranslationOptions)


class ProductFormTranslationOptions(TranslationOptions):
    fields = ("form_name",)


translator.register(ProductForm, ProductFormTranslationOptions)


class TypeTranslationOptions(TranslationOptions):
    fields = ("type_name",)


translator.register(Type, TypeTranslationOptions)


##################################WEBSITE########################
class TestimonailTranslationOptions(TranslationOptions):
    fields = ("content", "profile", "person", "job")


translator.register(Testimonail, TestimonailTranslationOptions)


class AdviceCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(AdviceCategory, AdviceCategoryTranslationOptions)


class AdviceTranslationOptions(TranslationOptions):

    fields = (
        "title",
        "content",
    )


translator.register(Advice, AdviceTranslationOptions)


class BannerTranslationOptions(TranslationOptions):

    fields = ("title", "content", "link_text")


translator.register(Banner, BannerTranslationOptions)


class BannerAboutUsTranslationOptions(TranslationOptions):

    fields = ("title", "content", "link_text")


translator.register(BannerAboutUs, BannerAboutUsTranslationOptions)


class IntroductionTranslationOptions(TranslationOptions):

    fields = ("context",)


translator.register(Introduction, IntroductionTranslationOptions)


class MissionTranslationOptions(TranslationOptions):

    fields = ("context",)


translator.register(Mission, MissionTranslationOptions)


class DirectorsGreetingsTranslationOptions(TranslationOptions):

    fields = ("context",)


translator.register(DirectorsGreetings, DirectorsGreetingsTranslationOptions)


class AboutUsCardsTranslationOptions(TranslationOptions):

    fields = (
        "title",
        "context",
    )


translator.register(AboutUsCards, AboutUsCardsTranslationOptions)


class HrBannerTranslationOptions(TranslationOptions):

    fields = ("title", "content", "link_text")


translator.register(HrBanner, HrBannerTranslationOptions)


class HrContentTranslationOptions(TranslationOptions):

    fields = (
        "title",
        "content",
    )


translator.register(HrContent, HrContentTranslationOptions)


class HrCardTranslationOptions(TranslationOptions):

    fields = ("title",)


translator.register(HrCard, HrCardTranslationOptions)


class TaniltsuulgaTranslationOptions(TranslationOptions):

    fields = ("title", "content")


translator.register(Taniltsuulga, TaniltsuulgaTranslationOptions)
