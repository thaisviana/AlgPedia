import os
import sys
import locale
import site

# get the virtualenv python packages
# site.addsitedir('/srv/projects/healthfollowup/env/lib/python2.7/site-packages')

#locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

sys.path.append('/home/algpedia/AlgPedia/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()