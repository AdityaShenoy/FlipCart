import rest_framework.status as rs  # type: ignore

from .create_response import create_response


USER_CREATED = create_response(
    "User Created",
    rs.HTTP_201_CREATED,
)
