from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound
from django.core.context_processors import csrf

from django.shortcuts import render_to_response
import os


def _getHTMLFormattedReuest(request, message="Disease Registry Default Page not found"):
    """
    Formats the request for display on debug pages.
    """
    return "<h1>{0}</h1> <pre>{1}</pre>".format(message, str(request))

def debug_handler404(request):
    """
    Returns simple 404 response with rendered request
    """
    return HttpResponseNotFound(_getHTMLFormattedReuest(request))

def debug_handler500(request):
    """
    Returns simple 500 response with rendered request
    """
    return HttpResponseServerError(_getHTMLFormattedReuest(request, "Disease Registry Default Server Error"))

def handler404(request):
    return render_to_response("404.html")

def handler500(request):
    return render_to_response("500.html")

# These views are for test and validation purposes.
# with debug = False, static data is not being served by django so the following views
# are provided to render nice test error pages which are not available in debug mode.
def test404(request):
    context = {}
    context.update(csrf(request))
    return render_to_response("404.html", context)

def test500(request):
    context = {}
    context.update(csrf(request))
    return render_to_response("500.html", context)
