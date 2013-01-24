from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^variation/", "registry.genetic.views.entry", {}, name="entry"),
)
