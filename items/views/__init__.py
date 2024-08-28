import rest_framework.views as rv  # type: ignore

from .get import get
from .get_id import get_id
from .post import post


class View(rv.APIView):
    def __init__(self):
        self.get = get
        self.post = post


class ViewId(rv.APIView):
    def __init__(self):
        self.get = get_id
