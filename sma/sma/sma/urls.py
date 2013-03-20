from django.conf import settings
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response

from django.contrib import admin

import django.contrib.auth
admin.autodiscover()


def variation_entry(request):
    return render_to_response("variation-entry/index.html")

urlpatterns = patterns('',
    (r'^genetic/', include("registry.genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}), 
    (r"^$", "django.views.generic.simple.direct_to_template", {"template": "sma/index.html"}),
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
