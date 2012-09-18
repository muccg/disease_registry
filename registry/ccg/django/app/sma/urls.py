from django.conf import settings
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response

import os


from django.contrib import admin
from ccg.utils import webhelpers as webhelpers

import django.contrib.auth
admin.autodiscover()
admin.site.root_path = webhelpers.url("/admin/")


def variation_entry(request):
    return render_to_response("variation-entry/index.html")

urlpatterns = patterns('',
    (r'^genetic/', include("genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}), 
)


urlpatterns += patterns('',
    (r"^$", "django.views.generic.simple.direct_to_template",
        {"template": "sma/index.html",
         "extra_context":{"INSTALL_NAME": 'sma', 'webhelpers': webhelpers}}),
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
