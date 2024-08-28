import rest_framework.status as rs  # type: ignore

from .create_response import create_response as create_response_


SUCCESS = create_response_(
    "SUCCESS",
    rs.HTTP_200_OK,
)
