"""
ASGI config for ontokproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import stream.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ontokproject.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        stream.routing.websocket_urlpatterns
    )
})
