"""
ASGI config for FlipCart project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import django.core.asgi as dca

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flip_cart.settings")

application = dca.get_asgi_application()
