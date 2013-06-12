from django.conf.urls import patterns
from django.conf.urls.defaults import include
from django.contrib import admin

urlpatterns = patterns('',
                       (r"^$", 'dm1.dm1.views.index'))

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls), {}),
                        )
