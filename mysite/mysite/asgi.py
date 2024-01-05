"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application

from chat.routing import websocket_urlpatterns
from chat.consumers import SayhelloConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import chat.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": OriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ,['*',]),
        "channel": ChannelNameRouter({
            "sayhello": SayhelloConsumer.as_asgi(),
        }),
    }
)
