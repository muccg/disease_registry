from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound

from django.shortcuts import render_to_response
import os

_TEMPLATE_PATH=""

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

def _getTemplatePath(name):
    """
    Returns the correct template path
    """
    return render_to_response(os.path.join(_TEMPLATE_PATH, name))

def handler404(request):
    return _getTemplatePath("404.html")

def handler500(request):
    return _getTemplatePath("500.html")
    
