import django.contrib.auth as dca
import django.http.request as dhreq

import flip_cart.constants.responses.auths as fcra


def post(request: dhreq.HttpRequest):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = dca.authenticate(request, username=username, password=password)
    if user:
        dca.login(request, user)
        return fcra.AUTH_SUCCESS
