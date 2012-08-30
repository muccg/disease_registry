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
#added 2012-06-20 for consent form: dm1_questionnaire/forms.py
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d/%m/%y',
                      '%d-%m-%Y', '%d-%m-%y',
                      '%d.%m.%Y', '%d.%m.%y', # this one doesn't work, probably needs to escape the '.'
                      '%d %m %Y', '%d %m %y',
                      '%d %b %Y',
                      '%Y-%m-%d'
                      )

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
RETURN_EMAIL = 'admin@ccg.murdoch.edu.au'
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
SESSION_COOKIE_AGE = 60*60
SESSION_COOKIE_PATH = url('/')
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_NAME = "csrftoken_registry"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False

# see https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
# https://docs.djangoproject.com/en/1.3/ref/settings/#std:setting-SESSION_FILE_PATH
# in production we would suggest using memcached for your session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = WRITABLE_DIRECTORY


#APPLICATION SPECIFIC SETTINGS
AUTH_PROFILE_MODULE = 'groups.User'
ROOT_URLCONF = 'registry.urls'
SITE_NAME = 'dm1'
SECRET_KEY = 'qj#tl@9@7((%^)$i#iyw0gcfzf&#a*pobgb8yr#1%65+*6!@g$'
EMAIL_APP_NAME = "Registry "

# INSTALL_NAME = 'registry' breaks templates/mako/admin/change_list.html in
# <link rel="stylesheet" type="text/css" media="screen" href="${ra.url('/static/css/%s_admin.css' % ra.get_current_install_name())}" />
# results in:
# <link rel="stylesheet" type="text/css" media="screen" href="/static/css/registry_admin.css" />
# registry_admin.css should be dm1_admin.css or dmd_admin.css
#INSTALL_NAME = 'registry'
####### change the app name here to run one or another
# caution, the DB params should be changed as well
INSTALL_NAME= 'dm1'
#INSTALL_NAME= 'dmd'
#INSTALL_NAME= 'sma'

if INSTALL_NAME == 'dm1':
    INSTALL_FULL_NAME = 'Australian Myotonic Dystrophy'
    INSTALLED_APPS.extend( [
        'groups',
        'patients',
        'genetic',
        'dm1',
        'dm1_questionnaire'
    ])

if INSTALL_NAME == 'dmd':
    INSTALL_FULL_NAME = 'Australian National Duchenne Muscular Dystrophy'
    INSTALLED_APPS.extend( [
        'groups',
        'patients',
        'genetic',
        'dmd'
    ])
if INSTALL_NAME == 'sma':
    INSTALL_FULL_NAME = 'Spinal Muscular Atrophy'
    INSTALLED_APPS.extend( [
        'groups',
        'patients',
        'genetic',
        'sma'
    ])

# A hash of application titles used as a global
# This could (should?) be provided by the apps themselves
APP_TITLES = {
"dmd": "DMD Registry",
"sma": "SMA Registry",
"dm1": "Myotonic Dystrophy Registry",
"dm1_questionnaire": "Online Questionnaire and Consent",
"patients": "Registration", # to show the 'Patients' header as 'Registration' in the Admin UI
}

# replaced by the code above
'''
#The ordering of these apps is important - they have been done in such a way that
#python manage.py migrate --all will work.
INSTALLED_APPS.extend( [
    'groups',
    'patients',
    'genetic',
#    'dmd',
#    'sma',
    'dm1',
    'dm1_questionnaire'
])
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'NAME': 'diseaseregistry',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
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
            'format': 'Registry [%(name)s:' + INSTALL_NAME + ':%(levelname)s:%(asctime)s:%(filename)s:%(lineno)s:%(funcName)s] %(message)s'
        },
        'db': {
            'format': 'Registry [%(name)s:' + INSTALL_NAME + ':%(duration)s:%(sql)s:%(params)s] %(message)s'
        },
        'simple': {
            'format': 'Registry ' + INSTALL_NAME + ' %(levelname)s %(message)s'
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

MEMCACHE_KEYSPACE = 'registryapp'

# Override defaults with local settings if available
try:
    from appsettings.registry import *
except ImportError, e:
    pass

DATABASES['default'] = DATABASES[INSTALL_NAME]
ROOT_APP = INSTALL_NAME
