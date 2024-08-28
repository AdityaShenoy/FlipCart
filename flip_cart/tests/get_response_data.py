import django.http.response as dhres

import typing as t


def get_response_data(response: dhres.HttpResponse) -> dict[str, t.Any]:
    return response.data  # type: ignore
