from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^genetic/', include("registry.genetic.urls"), {}),
    (r'^groups/', include("registry.groups.urls"), {}),
    (r'^humangenome/', include("registry.humangenome.urls"), {}),
    (r'^patients/', include("registry.patients.urls"), {}),
    
    # (r'^admin/', include(admin.site.urls), {}),
)
