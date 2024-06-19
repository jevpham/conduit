from .models import *
from rest_framework import serializers
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # Specifies the model to serialize
        fields = '__all__'  # Includes all fields of the Note model