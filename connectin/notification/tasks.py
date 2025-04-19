from celery import shared_task
from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

@shared_task
def send_ws_notification(username: str, body: str):
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(
        username,
        {
            "type": "notify",
            "message": body,
        }
    )
