# -*- coding: utf-8 -*-
# Base settings for local developer instances.

from base import *  # @UnusedWildImport
from django.core.servers import basehttp
import dj_database_url

USE_DJANGO_DEBUG_TOOLBAR = False
# Enable Django Debug Toolbar if the USE_DJANGO_DEBUG_TOOLBAR environment variable is set.
if USE_DJANGO_DEBUG_TOOLBAR and os.getenv('USE_DJANGO_DEBUG_TOOLBAR'):
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

# Enable the simple profiling middleware,
# which prints request duration and queries information to the console.
#MIDDLEWARE_CLASSES = (
#    'arranjei.util.profiling.SimpleProfilerMiddleware',
#) + MIDDLEWARE_CLASSES

# Disable runserver's default request logging to stdout.
basehttp.WSGIRequestHandler.log_message = lambda *args, **kwargs: None
