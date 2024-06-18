from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    # Create a UserSerializer instance with the data from the request
    serializer = UserSerializer(data=request.data)
    # Check if the provided data is valid according to the serializer's validation rules
    if serializer.is_valid():
        # Save the new user instance if the data is valid
        user = serializer.save()
        # Create a new token for the user or get the existing one
        token, created = Token.objects.get_or_create(user=user)
        # Return a JSON response with the token and a 201 Created status
        return JsonResponse({'token': token.key}, status=status.HTTP_201_CREATED)
    # If the data is not valid, return the errors with a 400 Bad Request status
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    # Get the email and password from the request data
    email = request.data.get('email')
    password = request.data.get('password')
    # Authenticate the user using the provided email and password
    user = authenticate(request, email=email, password=password)
    # If authentication is successful
    if user is not None:
        # Create a new token for the user or get the existing one
        token, created = Token.objects.get_or_create(user=user)
        # Return a JSON response with the token and a 200 OK status
        return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)
    # If authentication fails, return an error message with a 400 Bad Request status
    return JsonResponse({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
