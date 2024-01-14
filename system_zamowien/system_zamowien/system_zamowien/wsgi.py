"""
WSGI config for system_zamowien project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'system_zamowien.settings' if 'WEBSITE_HOSTNAME' in os.environ else 'system_zamowien.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()


