from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Notification

UserModel = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all() , write_only=True)
    class Meta:
        model = Notification
        fields = ['uid', 'body', 'user']