import rest_framework.response as rr  # type: ignore

import typing as t


def create_response(message: str, status: int, data: dict[str, t.Any] = {}):

    return rr.Response(data={"message": message, **data}, status=status)
