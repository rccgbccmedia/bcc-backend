from django.db import models

# Create your models here.
from accounts.models import User


class Event(models.Model):

    name = models.CharField(max_length=500, blank=False)
    venue = models.CharField(max_length=500, blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    capacity = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=False)
    photo_url = model.UrlField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta: 
        # Add verbose name 
        # verbose_name = 'Main Section'
        # verbose_name_plural = 'Main Section'
        ordering = ['-created']


class Rsvp(models.Model):

    event = models.OneToOneField(Event, related_name='events_rsvp', on_delete=models.CASCADE, blank=False)
    attendees = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return " possible attendance for %s" % self.event.name


