from django.conf.urls import patterns, include
from django.contrib import admin
from django.shortcuts import render_to_response
from django.conf import settings

import registry.urls as common_urls
from registry.common import views

admin.autodiscover() # very important so that registry admins (genetic, patient, etc) are discovered.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include("dmd.dmd.urls")),
    (r'', include(common_urls, namespace="registry")),
    (r'^iprestrict/', include('iprestrict.urls')),
    (r'^explorer/', include('explorer.urls')),
)

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}))


def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
