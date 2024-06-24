from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifies the model to serialize
        model = User 
        # Includes all fields of the User model
        fields = '__all__'  
        # Ensures the password field is write-only
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        # Create a new user instance using the validated data
        user = User.objects.create_user(**validated_data) 
        # Return the created user instance
        return user 
