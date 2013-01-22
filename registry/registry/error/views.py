from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.http import HttpResponceNotFound

import datetime

def _getHTMLFormattedReuest(request):
    """
    Formats the request for display on debug pages.
    """
    return "<h1>Page not found</h1> <pre> {} </pre>".format(str(request))

def debug_handler404(request):
    """
    Returns simple 404 response with body o request
    """
    return HttpResponseNotFound(_getHTMLFormattedReuest(request))

def debug_handler500(request):
    """
    Returns simple 500 response with body o request
    """
    return HttpResponseServerError(_getHTMLFormattedReuest(request))


def handler404(request):
    return render_to_response("error/404.html")

def handler500(request):
    return render_to_response("error/500.html")

