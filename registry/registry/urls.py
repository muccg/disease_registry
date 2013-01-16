from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    (r'^genetic/', include("registry.genetic.urls", namespace="genetic"), {}),
    (r'^groups/', include("registry.groups.urls"), {}),
    (r'^humangenome/', include("registry.humangenome.urls"), {}),
    (r'^patients/', include("registry.patients.urls", namespace="patients"), {}),
    
    # (r'^admin/', include(admin.site.urls), {}),
)
