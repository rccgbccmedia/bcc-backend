from django.test import TestCase
from .models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class ImageGetListAddTestCase(APITestCase):
    # create admin user
    self.admin = User(email='admin@mail', password='pass', is_superuser=True, is_staff=True)
    self.admin.save()