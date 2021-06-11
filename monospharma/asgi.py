import os

from django.conf import settings
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls.conf import re_path
from asgi_middleware_static_file import ASGIMiddlewareStaticFile
from django.conf.urls.static import static

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monospharma.settings.production")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from src.chat.consumers import ChatConsumer


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    url(r'^ws/(?P<room_name>[^/]+)/', ChatConsumer.as_asgi()),
                ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
            )
        ),
    }
)

application = ASGIMiddlewareStaticFile(
  application, static_url=settings.STATIC_URL,
  static_root_paths=[settings.STATIC_ROOT],
)

#application = ASGIMiddlewareStaticFile(
 # application, media_url=settings.MEDIA_URL,
  #media_root_paths=[settings.MEDIA_ROOT],
#)


