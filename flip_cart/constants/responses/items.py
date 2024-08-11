import rest_framework.status as rs  # type: ignore

from .create_response import create_response


ITEM_CREATED = create_response(
    "Item Created",
    rs.HTTP_201_CREATED,
)
