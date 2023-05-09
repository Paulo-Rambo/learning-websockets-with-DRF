from django.urls import path
from contador.consumers import CountConsumer

websocket_urlpatterns = [
    path('ws/count/', CountConsumer.as_asgi()),
]