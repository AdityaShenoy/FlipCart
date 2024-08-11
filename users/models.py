import django.contrib.auth.models as dcam
import django.db.models as ddm


class User(dcam.AbstractUser):
    username = ddm.CharField(max_length=50, unique=True)
    email = ddm.EmailField(max_length=50)
    password = ddm.CharField(max_length=50)
    first_name = ddm.CharField(max_length=50)
    last_name = ddm.CharField(max_length=50)
