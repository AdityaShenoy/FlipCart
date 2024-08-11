import django.urls as du

import auths.views as av

urlpatterns = [du.path("", av.View.as_view())]
