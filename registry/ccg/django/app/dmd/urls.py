from django.conf import settings
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response

import os


from django.contrib import admin
from ccg.utils import webhelpers as webhelpers

import django.contrib.auth
admin.autodiscover()
admin.site.root_path = webhelpers.url("/admin/")


def variation_entry(request):
    return render_to_response("variation-entry/index.html")

urlpatterns = patterns('',
    (r'^genetic/', include("genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}), 
)


urlpatterns += patterns('',
    (r"^$", "django.views.generic.simple.direct_to_template",
        {"template": "dmd/index.html",
         "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers}}),
)


urlpatterns += patterns('',
    (r"^nz[/]*$", "django.views.generic.simple.direct_to_template", {"template": "dmd/index_nz.html",
                                                               "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers},
                                                               })
)
# add the 2 sub pages from the main NZ page
urlpatterns += patterns('',
    (r"index_nz1$", "django.views.generic.simple.direct_to_template", {"template": "dmd/index_nz1.html",
                                                               "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers},
                                                               })
)
urlpatterns += patterns('',
    (r"index_nz2$", "django.views.generic.simple.direct_to_template", {"template": "dmd/index_nz2.html",
                                                               "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers},
                                                               })
)

# 2011-09-28 for special query
urlpatterns += patterns('', (r'^squery$', 'dmd.views.squery')) # string output for debug
urlpatterns += patterns('', (r'^squerycsv$', 'dmd.views.squerycsv')) # CSV file output

def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
