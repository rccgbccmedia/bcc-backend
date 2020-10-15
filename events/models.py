from django.db import models

# Create your models here.
from accounts.models import User


class Event(models.Model):

    name = models.CharField(max_length=500, blank=False, null=False)
    venue = models.CharField(max_length=500, blank=False, null=False)
    time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    capacity = models.BigIntegerField(blank=True)
    attendees = models.ManyToManyField(User, related_name='courses_joined', blank=True)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

   

    class Meta: 
        # Add verbose name 
        # verbose_name = 'Main Section'
        # verbose_name_plural = 'Main Section'
        ordering = ['-created']


# class Attendance(models.Model):

#     event = models.OneToOneField(Event, on_delete=models.CASCADE, blank=False)
#     attendees = models.ManyToManyField