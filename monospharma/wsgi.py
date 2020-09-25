"""
WSGI config for monospharma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/monospharm')
sys.path.append('/var/www/monospharm/monospharma')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monospharma.settings.production')

application = get_wsgi_application()
