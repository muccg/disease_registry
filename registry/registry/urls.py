from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    (r'^dm1/', include("ccg.django.app.dm1.urls"), {}),
    (r'^dmd/', include("ccg.django.app.dmd.urls"), {}),
    (r'^sma/', include("ccg.django.app.sma.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}),
)