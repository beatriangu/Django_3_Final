# chat/routing.py

from django.urls import re_path
from . import consumers  # Asegúrate de que este módulo exista y esté configurado correctamente

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
