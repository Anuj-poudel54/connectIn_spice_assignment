import json

from channels.generic.websocket import WebsocketConsumer

from django.contrib.auth.models import AnonymousUser


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        if user == AnonymousUser():
            self.close()
            return
        
        self.channel_name = user.username

        self.accept()
        self.send("Connected!")

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        ...
    
    def notify(self, event: dict):
        message = {
            "type": "notif",
            "message": event['message']
        } 

        self.send( text_data=json.dumps(message) )
