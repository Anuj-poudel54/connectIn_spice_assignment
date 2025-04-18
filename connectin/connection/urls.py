
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ConnectionApiView


urlpatterns = ([
    path('send/', ConnectionApiView.as_view({"post": "send_connection"}), name='send-connection-request'),
    path('decide/', ConnectionApiView.as_view({"post": "decide_connection"}), name='decide-connection-request'),
    path('list/<uuid:user_id>/', ConnectionApiView.as_view({"get": "list_by_user"}), name='decide-connection-request'),
])

