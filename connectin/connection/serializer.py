
from rest_framework import serializers

from .models import Connection

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("uid", "username")


class ConnectionListSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = Connection
        fields = ("uid", "from_user", "to_user", "accepted")

class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Connection
        fields = ("from_user", "to_user", "accepted")
