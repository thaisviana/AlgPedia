# -*- coding: utf-8 -*-
# Use this file as a basis for your local settings file.
# If you name it 'local.py', it will be used as the project's settings file automatically.
# If you use a different name, set the DJANGO_SETTINGS_MODULE environment variable
# to point to it (in Python dotted format).

# Pick one of the base settings files below, and remove the other lines:
from base import *  # @UnusedWildImport

LOCAL = False
DEBUG = False

# URL settings (optional).
HOST_NAME = 'algpedia.herokuapp.com'  # Only if your instance uses a hostname different than 'localhost'.
MEDIA_URL = '/media/'
STATIC_URL = '/algorithm/static/'

DATABASES = {'default': dj_database_url.config(default=os.environ['CLEARDB_DATABASE_URL'])}

# Email settings.
EMAIL_FROM_ADDRESS = 'AlgPedia <contato@algpedia.com.br>'  # All instances (except production) should set a custom sender name to it easier to distinguish where test email came from.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'algpedia'
    }
}

# DEFAULT_FILE_STORAGE = 'arranjei.util.s3utils.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
