from src.product.models import Product
from src.news.models import News, Category
from src.website.models import Gallery


def extras(request):
    newproduct = Product.objects.filter(is_product_new=True)
    gallery = Gallery.objects.all()
    news = News.objects.all()
    category = Category.objects.all()

    return {
        "newproduct": newproduct,
        "news_list": news,
        "gallery": gallery,
        "newscategory": category,
    }
