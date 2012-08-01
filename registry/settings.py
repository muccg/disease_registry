# -*- coding: utf-8 -*-
"""
Django settings defaults
"""
import os
from ccg.utils import webhelpers
from ccg.utils.webhelpers import url

# SCRIPT_NAME isnt set when not under wsgi
if not os.environ.has_key('SCRIPT_NAME'):
    os.environ['SCRIPT_NAME']=''

SCRIPT_NAME =   os.environ['SCRIPT_NAME']
PROJECT_DIRECTORY = os.environ['PROJECT_DIRECTORY']

#general site config
DEBUG = True
DEV_SERVER = True
SITE_ID = 1
APPEND_SLASH = True
SSL_ENABLED = False

# Locale
TIME_ZONE = 'Australia/Perth'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

##
## Django Core stuff
##
TEMPLATE_LOADERS = [
    'ccg.template.loaders.makoloader.filesystem.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    #'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    #'madas.utils.json_exception_handler_middleware.JSONExceptionHandlerMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'ccg.middleware.ssl.SSLRedirect'

]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_extensions',
    'south'
]

AUTHENTICATION_BACKENDS = [
 'django.contrib.auth.backends.ModelBackend',
]

#email
EMAIL_HOST = 'ccg.murdoch.edu.au'
SERVER_EMAIL = "apache@ccg.murdoch.edu.au"                      # from address
RETURN_EMAIL = "apache@ccg.murdoch.edu.au"                      # from address
EMAIL_SUBJECT_PREFIX = "DEV "
RETURN_EMAIL = 'bpower@ccg.murdoch.edu.au'
# default emails
ADMINS = [
    ( 'Tech Alerts', 'alerts@ccg.murdoch.edu.au' )
]
MANAGERS = ADMINS


# for local development, this is set to the static serving directory. For deployment use Apache Alias
STATIC_SERVER_PATH = os.path.join(PROJECT_DIRECTORY,"static")
# a directory that will be writable by the webserver, for storing various files...
WRITABLE_DIRECTORY = os.path.join(PROJECT_DIRECTORY,"scratch")
TEMPLATE_DIRS = [
    #os.path.join(PROJECT_DIRECTORY,"templates", "admin"),
    os.path.join(PROJECT_DIRECTORY,"templates"),
]
# mako compiled templates directory
MAKO_MODULE_DIR = os.path.join(WRITABLE_DIRECTORY, "templates")
# mako module name
MAKO_MODULENAME_CALLABLE = ''

MEDIA_ROOT = os.path.join(PROJECT_DIRECTORY,"static")
MEDIA_URL = '/static/'
ADMIN_MEDIA_PREFIX = url('/static/admin-media/')

TEMPLATE_DEBUG = DEBUG
LOGIN_URL = url('/accounts/login/')
LOGOUT_URL = url('/accounts/logout/')
LOGIN_REDIRECT_URL = url('/admin')


#session and cookies
MADAS_SESSION_TIMEOUT = 1800 #30 minute session timeout
SESSION_COOKIE_PATH = url('/')
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_NAME = "csrftoken_registry"
SESSION_COOKIE_AGE = 60*60
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False

#APPLICATION SPECIFIC SETTINGS
AUTH_PROFILE_MODULE = 'groups.User'
ROOT_URLCONF = 'registry.urls'
SITE_NAME = 'dm1'
SECRET_KEY = 'qj#tl@9@7((%^)$i#iyw0gcfzf&#a*pobgb8yr#1%65+*6!@g$'
EMAIL_APP_NAME = "Registry "

# set automagicaly by ccgbuild to either dmd_registry, dm1_registry or
# sma_registry
INSTALL_NAME = 'SET_THIS' # choices are 'dmd', 'dm1', 'sma'
INSTALL_FULL_NAMES = {'dmd': 'Australian National Duchenne Muscular Dystrophy',
                      'sma': 'Australian Spinal Muscular Atrophy',
                      'dm1': 'Australian Myotonic Dystrophy',
                      }

MODULE_INSTALLED_APPS = {
    "dmd": {"dmd": "DMD Registry"},
    "sma": {"sma": "SMA Registry"},
    "dm1": {
        "dm1": "Myotonic Dystrophy Registry",
        "dm1_questionnaire": "Online Questionnaire and Consent",
        "patients": "Registration", # to show the 'Patients' header as 'Registration' in the Admin UI
    },
}

#The ordering of these apps is important - they have been done in such a way that
#python manage.py migrate --all will work.
INSTALLED_APPS.extend( [
    'groups',
    'patients',
    'genetic',
])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
        'PORT': '',
    },
    'dmd_archive': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
        'PORT': '',
    },
    'sma': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
        'PORT': '',
    },
    'sma_archive': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
        'PORT': '',
    },
    'dm1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
        'PORT': '',
    },
    'dm1_archive': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': '<your db user>',
        'NAME': '<your db name>',
        'PASSWORD': '<your db password>',
        'HOST': '<your db host>',
    }
}
##
## LOGGING
##

LOG_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "logs")
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
            'format': 'Registry [%(name)s:%(levelname)s:%(asctime)s:%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
        },
        'db': {
            'format': 'Registry [%(name)s:%(duration)s:%(sql)s:%(params)s] %(message)s'
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
            'filename': os.path.join(LOG_DIRECTORY, 'madas_db.log'),
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
            'handlers': ['registryfile'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# Override defaults with your local instance settings.
# They will be loaded from appsettings.<projectname>, which can exist anywhere
# in the instance's pythonpath. This is a CCG convention designed to support
# global shared settings among multiple Django projects.
try:
    from appsettings.registry import *
except ImportError, e:
    pass

INSTALLED_APPS.extend(MODULE_INSTALLED_APPS[INSTALL_NAME].keys())

APP_TITLES = MODULE_INSTALLED_APPS[INSTALL_NAME]
DATABASES['default'] = DATABASES[INSTALL_NAME]
SECRET_KEY = "%s_%s" % (SECRET_KEY, INSTALL_NAME)
MEMCACHE_KEYSPACE = "%s_%s" % (INSTALL_NAME, MEMCACHE_KEYSPACE)
EMAIL_APP_NAME = "%s %s" % (INSTALL_NAME.upper(), EMAIL_APP_NAME)
CSRF_COOKIE_NAME = "%s_%s" % (CSRF_COOKIE_NAME, INSTALL_NAME)
