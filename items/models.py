import django.db.models as ddm

import users.models as um


class Item(ddm.Model):
    name = ddm.CharField(max_length=50)
    description = ddm.CharField(max_length=500)
    seller = ddm.ForeignKey(um.User, on_delete=ddm.CASCADE)
    mrp = ddm.IntegerField()
    price = ddm.IntegerField()
