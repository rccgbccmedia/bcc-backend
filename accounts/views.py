from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserRegistrationSerializer, UserDetailsSerializer, UserLoginSerializer
from rest_framework import generics
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from messaging.views import send_email
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                                PasswordResetConfirmView, PasswordResetView,
                                UserDetailsView)

# Create your views here.

# User Registration view
class UserRegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({'detail': 'User with that email already exists.'},status=status.HTTP_409_CONFLICT)
        headers = self.get_success_headers(serializer.data)
        send_email()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer

class UserDetailsView(generics.RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.
    Default accepted fields: username, first_name, last_name
    Read-only fields: pk, email
    Returns UserModel fields.
    """

    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)
    

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return get_user_model().objects.none()
