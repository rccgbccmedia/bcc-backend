from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import User
from .serializers import (UserRegistrationSerializer, UserDetailsSerializer, UserLoginSerializer, PasswordResetSerializer)
from rest_framework import generics
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from django.conf import settings


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

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework
    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    serializer_class = UserLoginSerializer

class UserDetailsView(generics.RetrieveUpdateAPIView):


    """
    get:
    Return a list of current user details.

    put:
    updates a the current user instance.
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


# password reset view
class PasswordResetView(PasswordResetView):
    serializer_class = PasswordResetSerializer


class ListUsersView(generics.ListAPIView):

    permission_classes = [IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
