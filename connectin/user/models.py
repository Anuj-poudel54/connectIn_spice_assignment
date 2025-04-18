from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser

from utils.models import BaseModel

# Create your models here.

class User(BaseModel, AbstractUser):
    address = models.TextField()
    industry = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
