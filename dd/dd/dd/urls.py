from django.conf import settings
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r"^$", "django.views.generic.simple.direct_to_template",{"template": "dd/index.html"})
)
