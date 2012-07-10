from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^variation/", "genetic.views.entry", {}),
)
