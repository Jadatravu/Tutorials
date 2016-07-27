"""
WSGI config for modelspro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site
try:
    site.addsitedir('/home/ubuntu/developer/dev_env/lib/python3.4/site-packages')

    sys.path.append('/home/ubuntu/developer/18Jul16/mypro')
    sys.path.append('/home/ubuntu/developer/18Jul16/mypro/mypro')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mypro.settings")
    # Activate your virtual env
    activate_env=os.path.expanduser("/home/ubuntu/developer/dev_env/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))
except Exception:
    print ("Exception occured")
    sys.exit(-1)






#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modelspro.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
