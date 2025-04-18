from rest_framework import serializers
from .models import User

from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'full_name', 'email', 'contact_number', 'address', 'industry', 'company_name']

    def validate_contact_number(self, value: str):
        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,7}$'
        validate = RegexValidator(pattern)

        if validate(value) is not None:
            raise serializers.ValidationError("Enter a valid contact number!")

        return value

