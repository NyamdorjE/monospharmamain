import os
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
        v_date = last.created_at.strftime("%Y-%m-%d %H:%M:%S")

    r = requests.get(
        "https://back.emonos.mn/api/product/root?manufacturer_id=10359&v_date=%s"
        % v_date
    )
    result = r.json()
    product_emonos(result)
    return HttpResponse("Successfully fetched", content_type="application/json")


def product_emonos(o_list, *args):
    for b in o_list:
        r = Product.objects.filter(product_id=b.get("erp_id")).first()
        if r is None:
            Product.objects.create(
                name=b.get("name"),
                photo=b.get("photo"),
                description=b.get("description"),
                ingredients=b.get("ingredients"),
                instructions=b.get("instructions"),
                warnings=b.get("warnings"),
                link="https://emonos.mn/product/%s" % b.get("product_id"),
            )
        else:
            r.name = b.get("name")
            r.photo = b.get("photo")
            r.description = b.get("description")
            r.ingredients = b.get("ingredients")
            r.instructions = b.get("instructions")
            r.warnings = b.get("warnings")
            r.save()
