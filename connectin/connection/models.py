from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel

# Create your models here.

userModel = get_user_model()

class Connection(BaseModel):
    from_user = models.ForeignKey(userModel, related_name="sent_requests", on_delete=models.CASCADE)
    to_user = models.ForeignKey(userModel, related_name="received_requests", on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("from_user", "to_user")
    
    def __str__(self):
        is_accepted = "Accepted" if self.accepted else "Pending"
        return f"{self.from_user.username} --> {self.to_user.username} | {is_accepted}"