from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the User model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the Note model
