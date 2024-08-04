"""
WSGI config for FlipCart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import django.core.wsgi as dcw
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FlipCart.settings")

application = dcw.get_wsgi_application()
