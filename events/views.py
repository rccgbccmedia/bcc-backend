from django.shortcuts import render, get_object_or_404
from .serializers import EventSerializer, RsvpSerializer
from rest_framework.response import Response
from .models import Event, Rsvp
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import isAdminOrReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny




# Create your views here.

class EventView(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [isAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        """
        create and event
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def destroy(self, request, *args, **kwargs):
        """
        Delete and event
        """
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


    def list(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            event_id = kwargs['pk']
            queryset = Rsvp.objects.filter(event = event_id)
        else:
            queryset = Rsvp.objects.filter(user = self.request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)