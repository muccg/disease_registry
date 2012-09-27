from django.conf import settings
from ccg.utils.webhelpers import url as django_url

def get_application_name(context, name):
    if name.lower() in settings.APP_TITLES:
        return settings.APP_TITLES[name.lower()]
    else:
        return name

def get_current_install_name(context):
    return settings.INSTALL_NAME

def get_full_registry_name(context):
    return settings.INSTALL_FULL_NAME

def url(context, url):
    return django_url(url)
