import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from django.contrib.auth.models import AnonymousUser


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        if user == AnonymousUser():
            self.close()
            return
        
        self.room_name = user.username
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)

        self.accept()
        self.send(f"Connected with channel name {self.room_name}!")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)

    def receive(self, text_data):
        ...
    
    def notify(self, event: dict):
        message = {
            "type": "notif",
            "message": event['message']
        } 

        self.send( text_data=json.dumps(message) )
