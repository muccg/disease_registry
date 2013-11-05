from django.conf.urls import patterns, include
from django.contrib import admin
from django.shortcuts import render_to_response

import registry.urls as common_urls
from registry.common import views

admin.autodiscover() # very important so that registry admins (genetic, patient, etc) are discovered.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include("dmd.dmd.urls")),
    (r'', include(common_urls, namespace="registry")),
    (r'^qbe/', include('django_qbe.urls')),
    (r'^iprestrict/', include('iprestrict.urls')),
    (r'^cdes/', include('rdrf_cdes.urls')),
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
