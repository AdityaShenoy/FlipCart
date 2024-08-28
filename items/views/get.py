import django.http.request as dhreq

import flip_cart.constants.responses as fcr
import flip_cart.constants.responses.create_response as fcrc

import items.models as im
import items.serializers as is_


def get(request: dhreq.HttpRequest):
    items = im.Item.objects.all()
    serialized_items = is_.ItemSerializer(items, many=True)
    return fcrc.create_data_response(
        fcr.SUCCESS,
        {"items": serialized_items.data},
    )
