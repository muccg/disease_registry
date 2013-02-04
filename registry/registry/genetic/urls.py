from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^variation/", "registry.genetic.views.entry", {}),
)
