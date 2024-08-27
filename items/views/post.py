import django.http.request as dhreq

import flip_cart.constants.responses.items as fcri

import items.models as im


def post(request: dhreq.HttpRequest):
    name = request.POST.get("name", "")
    description = request.POST.get("description", "")
    price = int(request.POST.get("price", 0))
    mrp = int(request.POST.get("price", 0))
    user = request.user
    im.Item.objects.create(
        name=name,
        description=description,
        price=price,
        mrp=mrp,
        seller=user,
    )
    return fcri.ITEM_CREATED
