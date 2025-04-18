from rest_framework import serializers
from .models import User

from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['uid', 'username', 'full_name', 'email', 'contact_number', 'address', 'industry', 'company_name', 'password']
    
    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_contact_number(self, value: str):
        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,7}$'
        validate = RegexValidator(pattern)

        if validate(value) is not None:
            raise serializers.ValidationError("Enter a valid contact number!")

        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
