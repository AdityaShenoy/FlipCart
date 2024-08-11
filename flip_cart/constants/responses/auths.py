import rest_framework.status as rs  # type: ignore

from .create_response import create_response


AUTH_SUCCESS = create_response(
    "Authentication Successful",
    rs.HTTP_200_OK,
)
