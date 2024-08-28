import rest_framework.serializers as rs  # type: ignore

import items.models as im


class ItemSerializer(rs.ModelSerializer):
    class Meta:
        model = im.Item
        fields = "__all__"
