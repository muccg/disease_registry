from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^genetic/', include("registry.genetic.urls")),
    url(r'^groups/', include("registry.groups.urls")),
    url(r'^humangenome/', include("registry.humangenome.urls")),
    url(r'^patients/', include("registry.patients.urls")),
    url(r'^errortest/', include("registry.common.urls")),
)
