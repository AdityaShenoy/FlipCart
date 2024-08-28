import django.http.request as dhreq

import flip_cart.constants.responses as fcr
import flip_cart.constants.responses.create_response as fcrc

import items.models as im
import items.serializers as is_


def get_id(request: dhreq.HttpRequest, id: int):
    item = im.Item.objects.get(pk=id)
    serialized_item = is_.ItemSerializer(item)
    return fcrc.create_data_response(
        fcr.SUCCESS,
        {"item": serialized_item.data},
    )
