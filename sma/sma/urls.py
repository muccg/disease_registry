from django.conf.urls.defaults import include
from django.conf.urls import patterns
from django.contrib import admin
from django.shortcuts import render_to_response

from registry.common import views as cviews

admin.autodiscover() # very important so that registry admins (genetic, patient, etc) are discovered.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include("sma.sma.urls")),
    (r'', include('registry.urls', namespace="registry")),
    (r'^qbe/', include('django_qbe.urls'))
)

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
