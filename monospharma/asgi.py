import os

from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monospharma.settings.production")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


import src.chat.routing


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app(),
        "websocket": AuthMiddlewareStack(
            URLRouter(src.chat.routing.websocket_urlpatterns)
        ),
    }
)
