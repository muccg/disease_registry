# -*- coding: utf-8 -*-
"""
Django settings defaults
"""
import os
from ccg_django_utils.conf import EnvConfig

env = EnvConfig()

SCRIPT_NAME = env.get("script_name", os.environ.get("HTTP_SCRIPT_NAME", ""))
FORCE_SCRIPT_NAME = env.get("force_script_name", "") or SCRIPT_NAME or None

WEBAPP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# General site config
PRODUCTION = env.get("production", False)
DEBUG = env.get("debug", not PRODUCTION)
TEMPLATE_DEBUG = DEBUG
DEV_SERVER = env.get("dev_server", not PRODUCTION)
SITE_ID = 1
APPEND_SLASH = env.get("append_slash", True)
SSL_ENABLED = env.get("ssl_enabled", PRODUCTION)

ROOT_URLCONF = env.get("root_urlconf", 'sma.urls')

SECRET_KEY = env.get("secret_key", "changeme")

# Locale
TIME_ZONE = 'Australia/Perth'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': env.get("dbuser", "registryapp"),
        'NAME': env.get("dbname", "sma"),
        'PASSWORD': env.get("dbpass", "registryapp"),
        'HOST': env.get("dbserver", "db"),
        'PORT': env.get("dbport", ""),
    }
}

# Django Core stuff
TEMPLATE_LOADERS = [
    'django.template.loaders.app_directories.Loader',
]

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
    'messages_ui',
    'userlog',
    'registry.groups',
    'registry.patients',
    'registry.genetic',
    'registry.common',
    'registry.configuration',
    'django.contrib.admin',
    'admin_views',
    'reversion',
    'iprestrict',
    'explorer',
]

# this needs to contain something like 'sma.sma' at a minimum
INSTALLED_APPS.extend(env.getlist("installed_apps"))

# these determine which authentication method to use
# apps use modelbackend by default, but can be overridden here
# see: https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
 'django.contrib.auth.backends.ModelBackend'
]

# email
EMAIL_USE_TLS = env.get("email_use_tls", False)
EMAIL_HOST = env.get("email_host", 'smtp')
EMAIL_PORT = env.get("email_port", 25)
EMAIL_APP_NAME = env.get("email_app_name", "Registry {0}".format(SCRIPT_NAME))
EMAIL_SUBJECT_PREFIX = env.get("email_subject_prefix", "DEV {0}".format(SCRIPT_NAME))

# default emails
ADMINS = [
    ('alerts', env.get("alert_email", "root@localhost"))
]
MANAGERS = ADMINS


STATIC_ROOT = env.get('static_root', os.path.join(WEBAPP_ROOT, 'static'))
STATIC_URL = '{0}/static/'.format(SCRIPT_NAME)

MEDIA_ROOT = env.get('media_root', os.path.join(WEBAPP_ROOT, 'static', 'media'))
MEDIA_URL = '{0}/static/media/'.format(SCRIPT_NAME)

# for local development, this is set to the static serving directory. For deployment use Apache Alias
STATIC_SERVER_PATH = os.path.join(WEBAPP_ROOT, "static")

# a directory that will be writable by the webserver, for storing various files...
WRITABLE_DIRECTORY = env.get("writable_directory", "/tmp")
try:
    if not os.path.exists(WRITABLE_DIRECTORY):
        os.mkdir(WRITABLE_DIRECTORY)
except:
    pass
os.path.exists(WRITABLE_DIRECTORY), "No writable directory, please create one: %s" % WRITABLE_DIRECTORY

# session and cookies
SESSION_COOKIE_AGE = env.get("session_cookie_age", 60 * 60)
SESSION_COOKIE_PATH = '{0}/'.format("SCRIPT_NAME")
SESSION_SAVE_EVERY_REQUEST = env.get("session_save_every_request", True)
SESSION_COOKIE_HTTPONLY = env.get("session_cookie_httponly", True)
SESSION_COOKIE_SECURE = env.get("session_cookie_secure", PRODUCTION)
SESSION_COOKIE_NAME = env.get("session_cookie_name", "registry_{0}".format(SCRIPT_NAME.replace("/", "")))

CSRF_COOKIE_NAME = env.get("csrf_cookie_name", "csrf_{0}".format(SESSION_COOKIE_NAME))

# see https://docs.djangoproject.com/en/dev/ref/settings/#session-engine
# https://docs.djangoproject.com/en/1.3/ref/settings/#std:setting-SESSION_FILE_PATH
# in production we would suggest using memcached for your session engine
SESSION_ENGINE = env.get("session_engine", 'django.contrib.sessions.backends.file')
SESSION_FILE_PATH = WRITABLE_DIRECTORY

# Testing settings
INSTALLED_APPS.extend(['django_nose'])
#TEST_RUNNER = 'sma.sma.tests.PatchedNoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = True
NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-branches',
    '--cover-package=sma',
]

# APPLICATION SPECIFIC SETTINGS
AUTH_PROFILE_MODULE = 'groups.User'

if env.get("memcache", ""):
    # memcache server list
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': env.getlist("memcache"),
            'KEYSPACE': env.get("keyspace", "registry-prod")
        }
    }
    CACHE_BACKEND = 'memcached://'+(';'.join(env.getlist("memcache")))+"/"

# #
# # LOGGING
# #
LOG_DIRECTORY = env.get('log_directory', os.path.join(WEBAPP_ROOT, "log"))
try:
    if not os.path.exists(LOG_DIRECTORY):
        os.mkdir(LOG_DIRECTORY)
except:
    pass
os.path.exists(LOG_DIRECTORY), "No log directory, please create one: %s" % LOG_DIRECTORY

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
            'filters': [],
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

EXPLORER_SQL_WHITELIST = ('UPDATE',)

EXPLORER_PERMISSION_VIEW = lambda u: u.is_superuser
EXPLORER_PERMISSION_CHANGE = lambda u: u.is_superuser

INTERNAL_IPS = ('127.0.0.1', '172.16.2.1')

ALLOWED_HOSTS = env.getlist("allowed_hosts", ["localhost"])

INSTALL_NAME = env.get("install_name", 'sma')

QBE_ACCESS_FOR = lambda user: user.is_superuser
LOGIN_URL = '{0}/admin'.format(SCRIPT_NAME)

try:
    print "Attempting to import default settings as appsettings.sma"
    from appsettings.sma import *
    print "Successfully imported appsettings.sma"
except ImportError, e:
    print "Failed to import appsettings.sma"
