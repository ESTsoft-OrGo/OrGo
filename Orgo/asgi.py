"""
ASGI config for app project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Orgo.settings')
django_asgi_app = get_asgi_application()

import chat.routing
import notify.routing
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns +
                notify.routing.websocket_urlpatterns
            )
        )
    ),
})