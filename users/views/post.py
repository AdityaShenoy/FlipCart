import django.http.request as dhreq

import flip_cart.constants.responses.users as fcru
import users.models as um


def post(request: dhreq.HttpRequest):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    um.User.objects.create_user(username=username, password=password)
    return fcru.USER_CREATED
