from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.conf import settings

from ccg.utils.webhelpers import url


def entry(request):
    context = {}
    context.update(csrf(request))
    context["base_url"] = url('/')  # should be able to use reverse but can't get it to work with the urls hooked in from admin
    context["CSRF_COOKIE_NAME"] = settings.CSRF_COOKIE_NAME
    return render_to_response("genetic/variation/index.html", context)
