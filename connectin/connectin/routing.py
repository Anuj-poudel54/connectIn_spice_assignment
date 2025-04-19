from django.urls import path

from notification.consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notifs/", NotificationConsumer.as_asgi()),
]