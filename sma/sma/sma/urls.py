from django.conf import settings
from django.conf.urls import *
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from django.contrib import admin

import views

import django.contrib.auth
admin.autodiscover()

def variation_entry(request):
    return render_to_response("variation-entry/index.html")

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name = "sma/index.html")),
    (r'^genetic/', include("registry.genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}),
    (r'^nmdreport/(?P<working_group>\w{2})$', views.nmd_report)
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
