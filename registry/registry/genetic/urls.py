from django.conf.urls.defaults import *

urlpatterns = patterns("",
    (r"^variation/", "ccg.django.app.genetic.views.entry", {}),
)
