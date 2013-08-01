from django.conf.urls import patterns
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    (r'^$', TemplateView.as_view(template_name = "fshd/index.html")),
)
urlpatterns += patterns(
    '',
    (r'^admin/', include(admin.site.urls), {}),
)
