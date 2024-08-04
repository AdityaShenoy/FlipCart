import django.urls as du

import users.views as uv


urlpatterns = [du.path("", uv.View.as_view())]
