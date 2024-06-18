from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the User model

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the Note model

