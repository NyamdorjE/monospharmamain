from src.product.models import Product
from src.news.models import News


def extras(request):
    newproduct = Product.objects.filter(is_product_new=True)
    news = News.objects.all()
    return {'newproduct': newproduct, 'news_list': news}
