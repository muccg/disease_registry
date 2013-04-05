from django.conf.urls.defaults import include
from django.conf.urls import patterns
from django.contrib import admin

from registry.common import views as cviews

admin.autodiscover() # very important so that registry admins (genetic, patient, etc) are discovered.

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include("sma.sma.urls")),
    (r'', include('registry.urls', namespace="registry")),
)

handler404 = cviews.handler404
handler500 = cviews.handler500
