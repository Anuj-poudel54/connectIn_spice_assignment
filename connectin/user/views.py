from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.

class UserCreate(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
