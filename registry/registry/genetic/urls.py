from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^variation/", "registry.genetic.views.entry", {}, name="entry"),
)
