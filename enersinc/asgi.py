<<<<<<< HEAD
=======
"""
ASGI config for enersinc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
>>>>>>> 311a2a502f7fe1b8b72a7a081fcf49d64aebb43d

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enersinc.settings')

application = get_asgi_application()
