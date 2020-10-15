from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def send_email():
    email = EmailMessage(
        'Title',
        'thanks for registering',
        settings.EMAIL_HOST_USER,
        ['dannynwangwu@gmail.com']
    )
    email.send(fail_silently=True)