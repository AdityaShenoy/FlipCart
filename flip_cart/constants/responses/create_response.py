import rest_framework.response as rr  # type: ignore

import typing as t


def create_response(message: str, status: int):

    return rr.Response(data={"message": message}, status=status)


def create_data_response(
    template_response: rr.Response,
    data: dict[str, t.Any],
):
    return rr.Response(
        data={**template_response.data, **data},  # type: ignore
        status=template_response.status_code,
    )
