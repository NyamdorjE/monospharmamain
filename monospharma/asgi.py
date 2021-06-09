import os

from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls.conf import re_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monospharma.settings.production")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


from src.chat.routing import ChatConsumer

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    re_path(
                        "ws/<str:room_name>/",
                        ChatConsumer.as_asgi(),
                    ),
                ]
            )
        ),
    }
)
