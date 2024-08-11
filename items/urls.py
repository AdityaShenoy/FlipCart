import django.urls as du

import items.views as iv


urlpatterns = [du.path("", iv.View.as_view())]
