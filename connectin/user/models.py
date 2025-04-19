from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import IntegrityError

from utils.models import BaseModel

# Create your models here.

class User(BaseModel, AbstractUser):
    address = models.TextField()
    industry = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True, unique=True)
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        try:
            return super().save(*args, **kwargs)
        except IntegrityError as e:

            if "UNIQUE constraint" in e.args[0]:
                self.username = self.full_name + "-" + str(self.uid)[:8]
                return super().save(*args, **kwargs)