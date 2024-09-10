from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *

class RegisterUserView(generics.CreateAPIView):
    # Define the queryset to be used for this view
    queryset = User.objects.all()
    # Specify the serializer class to be used
    serializer_class = UserSerializer
    # Allow any user to access this view
    permission_classes = [AllowAny]

    def create(self, request):
        # Get the serializer with the request data
        serializer = self.get_serializer(data=request.data)
        # Validate the serializer data
        serializer.is_valid(raise_exception=True)
        # Save the user instance
        user = serializer.save()
        # Create or get the token for the user
        token, created = Token.objects.get_or_create(user=user)
        # Get the success headers
        headers = self.get_success_headers(serializer.data)
        # Return the response with the token and status code
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

class LoginUserView(generics.GenericAPIView):
    # Specify the serializer class to be used
    serializer_class = UserSerializer
    # Require the user to be authenticated to access this view
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the email and password from the request data
        email = request.data.get('email')
        password = request.data.get('password')
        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Create or get the token for the user
            token, created = Token.objects.get_or_create(user=user)
            # Return the response with the token and status code
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        # Return the response with an error message and status code
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request):
    #     return Response({'message': 'Hello, World!'})
    
    # def put(self, request):
    #     return Response({'message': 'Hello, World!'})
    