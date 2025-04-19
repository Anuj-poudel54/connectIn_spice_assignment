from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel
# Create your models here.

UserModel = get_user_model()

class Notification(BaseModel):
    user = models.ForeignKey(UserModel, related_name='notifications', on_delete=models.CASCADE)
    body = models.TextField()
    notified = models.BooleanField(default = False)
