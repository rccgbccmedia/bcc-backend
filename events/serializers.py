from rest_framework import serializers
from .models import Event, Rsvp

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields= '__all__'
        # read_only_fields = ['attendees']

class RsvpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rsvp
        fields = '__all__'
        read_only_fields = ['seat', 'user']