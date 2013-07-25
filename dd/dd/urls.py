from django.conf.urls import include
from django.conf.urls import patterns
from django.contrib import admin
from django.conf import settings
from django.shortcuts import render_to_response

import registry.urls

admin.autodiscover() #very important so that registry admins (genetic, patient, etc) are discovered.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls), {}),
    (r'^$', include("dd.dd.urls"), {}),
    (r'', include(registry.urls, namespace="registry")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^iprestrict/', include('iprestrict.urls')),
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
