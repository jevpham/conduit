from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Includes all fields in the User model.
    """
    class Meta:
        model = User  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the User model

class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model.
    Includes all fields in the Note model.
    """
    class Meta:
        model = Note  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the Note model

