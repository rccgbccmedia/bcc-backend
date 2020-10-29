from django.db import models

# Create your models here.
from accounts.models import User


class Event(models.Model):

    name = models.CharField(max_length=500, blank=False)
    venue = models.CharField(max_length=500, blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    capacity = models.BigIntegerField(blank=True, null=True)
    seats = models.BigIntegerField(blank=True, null=True, default = 0)
    description = models.TextField(blank=False)
    photo_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta: 
        # Add verbose name 
        # verbose_name = 'Main Section'
        # verbose_name_plural = 'Main Section'
        ordering = ['-created']


class Rsvp(models.Model):

    event = models.ForeignKey(Event, related_name='events_rsvp', on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, blank=False, related_name='rsvp_user', on_delete=models.CASCADE)
    seat = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return " RSVP for %s" % self.event.name


