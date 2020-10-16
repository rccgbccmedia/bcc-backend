from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Event
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import isAdminOrReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny




# Create your views here.

class EventView(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [isAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("event deleted", status=status.HTTP_204_NO_CONTENT)
