import rest_framework.views as rv  # type: ignore

from .post import post


class View(rv.APIView):
    def __init__(self):
        self.post = post
