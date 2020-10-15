from django.shortcuts import render
from .serializers import EventSerializer
from .models import Event
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet



# Create your views here.

class EventView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer