#!/usr/bin/python

import sys
import site
import os


VIRTUALENV = '/home/ubuntu/.virtualenvs/valpo/lib/python2.7/site-packages'
WEBAPPS_PATH ='/home/ubuntu/valporank'

prev_sys_path = list(sys.path)

# add the site-packages of our virtualenv as a site dir
site.addsitedir(VIRTUALENV)

# add the app's directory to the PYTHONPATH
sys.path.append(WEBAPPS_PATH)

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

# import from down here to pull in possible virtualenv django install
os.environ['DJANGO_SETTINGS_MODULE'] = 'valporank.configs'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

