from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^test404/", "registry.errors.views.test404", {}),
    url(r"^test500/", "registry.errors.views.test500", {}),
)
