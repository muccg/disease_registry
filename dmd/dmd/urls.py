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
)

handler404 = views.handler404
handler500 = views.handler500
