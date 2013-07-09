from django.conf.urls import patterns
from django.conf.urls import include
from django.contrib import admin

urlpatterns = patterns('',
                       (r"^$", "django.views.generic.simple.direct_to_template",
                        {"template": "fshd/index.html"}))

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls), {}),
                        )
