# -*- coding: utf-8 -*-
"""
Django settings defaults
"""
import os

WEBAPP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# General site config
DEBUG = True
DEV_SERVER = True
SITE_ID = 1
APPEND_SLASH = True
SSL_ENABLED = False


# Locale
TIME_ZONE = 'Australia/Perth'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

ROOT_URLCONF = 'dd.urls'
SECRET_KEY = 'f136ebd30113056c8deba7e1f7944bdf'

# Django Core stuff
TEMPLATE_LOADERS = [
    'django.template.loaders.app_directories.Loader',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'registryapp',
        'NAME': 'dd',
        'PASSWORD': 'registryapp',
        'HOST': '',
        'PORT': '',
    }
}

# see: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'ccg.middleware.ssl.SSLRedirect',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# see: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_extensions',
    'south',
    'userlog',
    'registry.groups',
    'registry.patients',
    'registry.genetic',
    'registry.common',
    'dd.dd',
    'progressbarupload',
    'django.contrib.admin',
]


# these determine which authentication method to use
# apps use modelbackend by default, but can be overridden here
# see: https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
 'django.contrib.auth.backends.ModelBackend'
]

# email
EMAIL_HOST = 'ccg.murdoch.edu.au'
SERVER_EMAIL = "apache@ccg.murdoch.edu.au"  # from address
RETURN_EMAIL = 'web@ccg.murdoch.edu.au'

# default emails
ADMINS = [
    ('Tech Alerts', 'alerts@ccg.murdoch.edu.au')
]
MANAGERS = ADMINS


STATIC_ROOT = os.path.join(WEBAPP_ROOT, 'static')
STATIC_URL = '{0}/static/'.format(os.environ.get("SCRIPT_NAME", ""))

MEDIA_ROOT = os.path.join(WEBAPP_ROOT, 'media')
MEDIA_URL = '{0}/media/'.format(os.environ.get("SCRIPT_NAME", ""))

# for local development, this is set to the static serving directory. For deployment use Apache Alias
STATIC_SERVER_PATH = os.path.join(WEBAPP_ROOT, "static")

# a directory that will be writable by the webserver, for storing various files...
WRITABLE_DIRECTORY = "/tmp"
TEMPLATE_DEBUG = DEBUG

# session and cookies
SESSION_COOKIE_AGE = 60 * 60
SESSION_COOKIE_PATH = '{0}/'.format(os.environ.get("SCRIPT_NAME", ""))
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_NAME = "csrftoken_registry"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False

SESSION_COOKIE_NAME = "registry_dd"

# see https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
# https://docs.djangoproject.com/en/1.3/ref/settings/#std:setting-SESSION_FILE_PATH
# in production we would suggest using memcached for your session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = WRITABLE_DIRECTORY

FILE_UPLOAD_HANDLERS = (
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# APPLICATION SPECIFIC SETTINGS
AUTH_PROFILE_MODULE = 'groups.User'
EMAIL_APP_NAME = "Registry "

# #
# # LOGGING
# #
LOG_DIRECTORY = os.path.join(WEBAPP_ROOT, "logs")
try:
    if not os.path.exists(LOG_DIRECTORY):
        os.mkdir(LOG_DIRECTORY)
except:
    pass
os.path.exists(LOG_DIRECTORY), "No logs directory, please create one: %s" % LOG_DIRECTORY

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': 'Registry [%(levelname)s:%(asctime)s:%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
        },
        'db': {
            'format': 'Registry [%(duration)s:%(sql)s:%(params)s] %(message)s'
        },
        'simple': {
            'format': 'Registry %(levelname)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'errorfile':{
            'level':'ERROR',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIRECTORY, 'error.log'),
            'when':'midnight',
            'formatter': 'verbose'
        },
        'registryfile':{
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIRECTORY, 'registry.log'),
            'when':'midnight',
            'formatter': 'verbose'
        },
        'db_logfile':{
            'level':'DEBUG',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIRECTORY, 'registry_db.log'),
            'when':'midnight',
            'formatter': 'db'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'verbose',
            'include_html':True
        }
    },
    'root': {
            'handlers':['console', 'errorfile', 'mail_admins'],
            'level':'ERROR',
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'registry_log': {
            'handlers': ['registryfile', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}


################################################################################
## Customize settings for each registry below
################################################################################

INSTALL_NAME = 'dd'

try:
    print "Attempting to import local settings as appsettings.dd"
    from appsettings.dd import *
    print "Successfully imported appsettings.dd"
except ImportError, e:
    print "Failed to import appsettings.dd"
