# -*- coding: utf-8 -*-
# Use this file as a basis for your local settings file.
# If you name it 'local.py', it will be used as the project's settings file automatically.
# If you use a different name, set the DJANGO_SETTINGS_MODULE environment variable
# to point to it (in Python dotted format).

# Pick one of the base settings files below, and remove the other lines:

from development import * # @UnusedWildImport

LOCAL = True

# DEFAULT_FILE_STORAGE = 'arranjei.util.s3utils.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'arranjei.util.s3utils.StaticRootS3BotoStorage'

MEDIA_ROOT = 'media/'

# URL settings (optional).
HOST_NAME = 'localhost:8000' # Only if your instance uses a hostname different than 'localhost'.
# MEDIA_URL = 'http://arranjei-pa.s3.amazonaws.com/'
MEDIA_URL = '/media/'
STATIC_URL = '/algorithm/static/'


# Database settings.
DATABASES['default'] = dj_database_url.config(env='DATABASE_URL', default='mysql://root:mysql3306@localhost:3306/AlgPedia')

# Email settings.
EMAIL_FROM_ADDRESS = 'Arranjei <contato@ensaiolegal.com.br>' # All instances (except production) should set a custom sender name to it easier to distinguish where test email came from.
DETOUR_EMAIL_ADDRESS = 'Pablo Abdelhay <pabdelhay@inoa.com.br>' # Developer instances should set the catch-all address to avoid having mail sent to the whole development team.

CACHES = {
'default': {
'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
'LOCATION': 'algpedia'
}
}
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'AlgPedia',
'USER': 'root',
'PASSWORD': '123mudar',
'HOST': '127.0.0.1', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
'PORT': '3306', # Set to empty string for default.
}
}
