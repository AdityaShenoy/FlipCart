import rest_framework.response as rr  # type: ignore

import typing as t


class CustomResponse(rr.Response):
    data: dict[str, t.Any] = dict()


def create_response(message: str, status: int):

    return rr.Response(data={"message": message}, status=status)


def create_data_response(
    template_response: CustomResponse,
    data: dict[str, t.Any],
):
    return CustomResponse(
        data={**template_response.data, **data},
        status=template_response.status_code,
    )
