from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from events.models import Event
from accounts.models import User



# Create your views here.



def send_event_details(rsvp):
    event = get_object_or_404(Event, pk=rsvp['event'])
    user = get_object_or_404(User, pk = rsvp['user'])
    seat_number = rsvp['seat']

    context = {
        'seat_number' : seat_number,
        'event_location' : event.venue,
        'event_date' : event.time.date().strftime("%B %d %Y"),
        'event_time' : event.time.time().strftime("%-I:%M %p"),
        'event_name' : event.name,
    }
    msg_html = render_to_string('new_registration.html',context)
    send_mail(
        'Event Reservation',
        strip_tags(msg_html),
        settings.EMAIL_HOST_USER,
        [user.email,],
        fail_silently=False,
        html_message = msg_html,
    )