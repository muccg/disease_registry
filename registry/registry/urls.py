from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    #(r'^dm1/', include("registry.dm1.urls"), {}),
    #(r'^dmd/', include("registry.dmd.urls"), {}),
    #(r'^sma/', include("registry.sma.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}),
)
