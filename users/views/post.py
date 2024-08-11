import django.http.request as dhreq

import flip_cart.constants.responses.users as fcru
import users.models as um


def post(request: dhreq.HttpRequest):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    first_name = request.POST.get("first_name", "")
    last_name = request.POST.get("last_name", "")
    um.User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    return fcru.USER_CREATED
