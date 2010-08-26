# -*- coding: utf-8 -*-
# Django settings for satchmo project.
# If you have an existing project, then ensure that you modify local_settings-customize.py
# and import it from your main settings file. (from local_settings import *)
import os
import logging

LOCAL_DEV = True 
DEBUG = True
TEMPLATE_DEBUG = DEBUG


DIRNAME = os.path.dirname(__file__)

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)

SATCHMO_DIRNAME = DIRNAME


DJANGO_PROJECT = 'rinconcolombia'
DJANGO_SETTINGS_MODULE = 'rinconcolombia.settings'

ADMINS = (
     ('Ariel Núñez', 'ingenieroariel@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# The following variables should be configured in your local_settings.py file
#DATABASE_NAME = ''             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(DIRNAME, 'rinconcolombia.db')



# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'America/Bogota'

USE_I18N = True

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'es'
gettext = lambda s: s

LANGUAGES = (
    ('es', gettext('Spanish')),
    ('en', gettext('English')),
)

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#Image files will be stored off of this path
MEDIA_ROOT = os.path.join(DIRNAME, 'static/')
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
#MEDIA_URL = 'site_media'
MEDIA_URL="/static/"
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f5%haw72nh6#m2xgvg37(6=^lj_7-v40fcpcx+#4oft23w=9i*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    "satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    #'djangologging.middleware.LoggingMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, "templates"),
)


#this is used to add additional config variables to each request
# NOTE: overridden in local_settings.py
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = ('satchmo_store.shop.context_processors.settings',
                               'django.core.context_processors.auth',
                               'satchmo_ext.recentlist.context_processors.recent_products',
                               'django.core.context_processors.i18n',
                          )

#ROOT_URLCONF = 'satchmo.urls'
ROOT_URLCONF = 'rinconcolombia.urls'

INSTALLED_APPS = (
    'django.contrib.sites',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'registration',
    'sorl.thumbnail',
    'keyedcache',
    'livesettings',
    'l10n',
    'satchmo_utils.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    'satchmo_store.contact.supplier',
    'shipping.modules.tiered',
    'shipping.modules.tieredweight',
    'satchmo_ext.newsletter',
    'satchmo_ext.recentlist',
    'testimonials',
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    'product.modules.downloadable',
    'product.modules.subscription',
    'satchmo_ext.product_feeds',
    'satchmo_ext.brand',
    'payment',
    'payment.modules.purchaseorder',
    'payment.modules.paypal',
    'payment.modules.giftcertificate',
    'satchmo_ext.wishlist',
    'satchmo_ext.upsell',
    'satchmo_ext.productratings',
    'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    'shipping.modules.tieredquantity',
    'django_extensions',
    'satchmo_ext.tieredpricing',
    'typogrify',
    #'debug_toolbar',
    'app_plugins',
    'cpserver',
    'rinconcolombia.localsite',
    'django.contrib.flatpages',
)

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False,
}

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE' : '/',
    'MULTISHOP' : False,
    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "S"

ACCOUNT_ACTIVATION_DAYS = 7

#Configure logging
LOGFILE = "satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

#fileLog = logging.FileHandler(os.path.join(DIRNAME, LOGFILE), 'w')
#fileLog.setLevel(logging.DEBUG)
# add the handler to the root logger
#logging.getLogger('').addHandler(fileLog)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.info("Satchmo Started")

#Keys from keyczar
ENCRYPTED_FIELD_KEYS_DIR= os.path.join(DIRNAME, 'keys/')

try:
    # Load the local settings
    from local_settings import *
except:
    #Do not spit an error if this file is not found
    pass

