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
    (r"^[/]*$", "django.views.generic.simple.direct_to_template", {"template": "%s/index.html" % settings.INSTALL_NAME,
                                                               "extra_context":{"INSTALL_NAME": settings.INSTALL_NAME, 'webhelpers': webhelpers},
                                                               }),

    (r'^genetic/', include("genetic.urls"), {}),
    (r'^admin/', include(admin.site.urls), {}), 

)

# add the New Zealand splash if DMD
if settings.INSTALL_NAME == 'dmd':
    urlpatterns += patterns('',
        (r"^nz[/]*$", "django.views.generic.simple.direct_to_template", {"template": "%s/index_nz.html" % settings.INSTALL_NAME,
                                                                   "extra_context":{"INSTALL_NAME": settings.INSTALL_NAME, 'webhelpers': webhelpers},
                                                                   })
    )
    # add the 2 sub pages from the main NZ page
    urlpatterns += patterns('',
        (r"index_nz1$", "django.views.generic.simple.direct_to_template", {"template": "%s/index_nz1.html" % settings.INSTALL_NAME,
                                                                   "extra_context":{"INSTALL_NAME": settings.INSTALL_NAME, 'webhelpers': webhelpers},
                                                                   })
    )
    urlpatterns += patterns('',
        (r"index_nz2$", "django.views.generic.simple.direct_to_template", {"template": "%s/index_nz2.html" % settings.INSTALL_NAME,
                                                                   "extra_context":{"INSTALL_NAME": settings.INSTALL_NAME, 'webhelpers': webhelpers},
                                                                   })
    )

    # 2011-09-28 for special query
    urlpatterns += patterns('', (r'^squery$', 'dmd.views.squery')) # string output for debug
    urlpatterns += patterns('', (r'^squerycsv$', 'dmd.views.squerycsv')) # CSV file output

# Add the questionnaire if DM1.
if settings.INSTALL_NAME == "dm1":
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
