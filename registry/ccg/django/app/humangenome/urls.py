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
    (r'^genetic/', include("ccg.django.app.genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}), 
)

if hasattr(settings, 'ROOT_APP'):
    urlpatterns += patterns('',
        (r"^[/]*$", "django.views.generic.simple.direct_to_template",
            {"template": "%s/index.html"%(settings.ROOT_APP),
             "extra_context":{"INSTALL_NAME": settings.ROOT_APP, 'webhelpers': webhelpers}}),
    )
else:
    urlpatterns += patterns('',
        (r"^dmd/", "django.views.generic.simple.direct_to_template",
            {"template": "dmd/index.html",
             "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers}}),

        (r"^sma/", "django.views.generic.simple.direct_to_template",
            {"template": "sma/index.html",
             "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers}}),
                                                              
        (r"^dm1/", "django.views.generic.simple.direct_to_template",
            {"template": "dm1/index.html",
             "extra_context":{"INSTALL_NAME": 'dmd', 'webhelpers': webhelpers}}),
    )

# add the New Zealand splash if DMD
if 'dmd' in settings.INSTALLED_APPS:
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
    urlpatterns += patterns('', (r'^squery$', 'ccg.django.app.dmd.views.squery')) # string output for debug
    urlpatterns += patterns('', (r'^squerycsv$', 'ccg.django.app.dmd.views.squerycsv')) # CSV file output

# Add the questionnaire if DM1.
if "dm1" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        (r"^questionnaire/", include("dm1_questionnaire.urls")),
    )


# serve static with django server in devel
if settings.DEBUG:
    urlpatterns += patterns('',
        (r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.STATIC_SERVER_PATH, "show_indexes": True})
    )


def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")
