import os
from django.db.models.aggregates import Count
import requests
import json
from django.http import HttpResponse


from src.product.models import Product, ProductCategory


def product_fetch(request=None):
    """
    Бүтээгдэхүүний татах emonos.mn

    """
    v_date = "2015-01-01 00:00:00"
    last = Product.objects.order_by("-created_on").first()
    if last is not None:
        v_date = last.created_on.strftime("%Y-%m-%d %H:%M:%S")

    r = requests.get(
        "https://back.emonos.mn/api/product/root?manufacturer_id=10359&v_date=%s"
        % v_date
    )
    result = r.json()
    product_emonos(result)
    print(result)
    return HttpResponse("Successfully fetched", content_type="application/json")


def product_emonos(o_list, *args):
    for b in o_list:
        r = Product.objects.filter(product_id=b.get("erp_id")).first()
        print(r)
        if r is None:
            Product.objects.create(
                product_id=b.get("erp_id"),
                name=b.get("name"),
                photo=b.get("photo"),
                description=b.get("description"),
                ingredients=b.get("ingredients"),
                instructions=b.get("instructions"),
                warnings=b.get("warnings"),
                price=b.get("price"),
                link="https://emonos.mn/product/%s" % b.get("product_id"),
            )
            print("created")
        else:
            print("updated")
            r.name = b.get("name")
            r.photo = b.get("photo")
            r.description = b.get("description")
            r.ingredients = b.get("ingredients")
            r.instructions = b.get("instructions")
            r.price = b.get("price")
            r.warnings = b.get("warnings")
            r.save()
