from django.shortcuts import render, get_object_or_404
from .serializers import EventSerializer, RsvpSerializer
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
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("event deleted", status=status.HTTP_204_NO_CONTENT)

class RsvpView(ModelViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RsvpSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Rsvp for an event
        """
        event = get_object_or_404(Event, pk=kwargs['pk'])
        event.seats += 1
        event.save()
        seat_number = event.seats
        rsvp = {'event': kwargs['pk'], 'seat':seat_number, 'user': request.user.id}
        serializer = self.get_serializer(data=rsvp)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
