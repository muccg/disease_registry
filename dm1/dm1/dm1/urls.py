from django.conf.urls import patterns
from django.conf.urls.defaults import include
from django.contrib import admin

urlpatterns = patterns('',
                       (r"^$", "django.views.generic.simple.direct_to_template",
                        {"template": "dm1/index.html"}))

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls), {}),
                        )
