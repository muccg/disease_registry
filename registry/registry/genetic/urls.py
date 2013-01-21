from django.conf.urls import patterns

urlpatterns = patterns("",
    url(r"^variation/", "registry.genetic.views.entry", {}, name="entry"),
)
