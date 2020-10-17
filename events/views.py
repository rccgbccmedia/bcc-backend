from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Event, Rsvp
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import isAdminOrReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny




# Create your views here.

class EventView(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [isAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(serializer.data)
        event_id = serializer.data["id"]
        event = Event.objects.get(id=event_id)
        rsvp = Rsvp(event = event)
        rsvp.save(force_insert=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("event deleted", status=status.HTTP_204_NO_CONTENT)

    def rsvp(self, request, *args, **kwargs):
        event = self.get_object()
        user = request.user
        rsvp = event.events_rsvp
        rsvp.attendees.add(user)
        print(rsvp)
        return Response("registeration for event successful", status=status.HTTP_201_CREATED)
