
from django.urls import path


from .views import ConnectionApiView


urlpatterns = ([
    path('accepted/', ConnectionApiView.as_view({"get": "list_connections"}), name='list-accepted-request'),
    path('send/', ConnectionApiView.as_view({"post": "send_connection"}), name='send-connection-request'),
    path('decide/', ConnectionApiView.as_view({"post": "decide_connection"}), name='decide-connection-request'),
    path('requests/', ConnectionApiView.as_view({"get": "list_request"}), name='list-connection-requests'),
    path('sent-requests/', ConnectionApiView.as_view({"get": "list_sent_request"}), name='list-sent-connection-requests'),
])

