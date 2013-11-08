import os
import sys
import locale
import site

# get the virtualenv python packages
site.addsitedir('/home/algpedia/AlgPedia/env/lib/python2.7/site-packages')

sys.path.append('/home/algpedia/AlgPedia/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

activate_env=os.path.expanduser('/home/algpedia/AlgPedia/env/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()