from django.conf.urls import patterns, include
from django.shortcuts import render_to_response
from django.contrib import admin
from django.views.generic.base import TemplateView

import views

import registry
import registry.urls


admin.autodiscover()

def variation_entry(request):
    return render_to_response("variation-entry/index.html")

urlpatterns = patterns('',
    (r"^$", TemplateView.as_view(template_name='dmd/index.html')),
)

# 2011-09-28 for special query
urlpatterns += patterns('', (r'^squery/(?P<working_group>\w{2})$', views.squery))  # string output for debug
urlpatterns += patterns('', (r'^squerycsv/(?P<working_group>\w{2})$', views.squerycsv))  # CSV file output

