import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'exnihilo.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/divye/src/git/exnihilo'
if path not in sys.path:
    sys.path.append(path)
