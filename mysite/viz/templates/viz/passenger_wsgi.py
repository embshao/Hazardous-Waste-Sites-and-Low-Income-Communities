dirpath = '/home/embarnard/mejo583.embarnardshao.com' # Leave the trailing slash OFF!
project_name = 'mysite'

# -----------------

import sys, os

sys.path.append(dirpath + '/')
sys.path.append(dirpath + '/' + project_name)

INTERP = os.path.expanduser(dirpath + "/env/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,dirpath + '/env/bin')
sys.path.insert(0,dirpath + '/env/lib/python3.6.5/site-packages/django')
sys.path.insert(0,dirpath + '/env/lib/python3.6.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = project_name + ".settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
