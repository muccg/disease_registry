# Generic WSGI application
import os
import django.core.handlers.wsgi

def application(environ, start):

    # copy any vars into os.environ
    for key in environ:
        os.environ[key] = str(environ[key])

    # legacy cruft from the rpm wsgi file
    if "HTTP_SCRIPT_NAME" in environ:
        environ['SCRIPT_NAME']=environ['HTTP_SCRIPT_NAME']
        os.environ['SCRIPT_NAME']=environ['HTTP_SCRIPT_NAME']
    else:
        os.environ['SCRIPT_NAME']=environ['SCRIPT_NAME']

    return django.core.handlers.wsgi.WSGIHandler()(environ,start)
