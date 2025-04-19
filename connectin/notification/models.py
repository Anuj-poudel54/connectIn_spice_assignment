from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel
from .tasks import send_ws_notification

# Create your models here.

UserModel = get_user_model()

class Notification(BaseModel):
    user = models.ForeignKey(UserModel, related_name='notifications', on_delete=models.CASCADE)
    body = models.TextField()

    def notify_user(self):
        send_ws_notification.delay(self.user.username, self.body)
