from django.test import TestCase
from accounts.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class ImageGetListAddTestCase(APITestCase):
    def setUp(self):
        # create a new user by making a post request to register endpoint
        self.user=self.client.post('/register/',data={'email':'mario@testmail.com','password':'i-keep-jumping', 'first_name':'mario', 'last_name':'icardi', 'phone': '+2348122633167', 'address': "here"})
        # obtain a json web token for the newly created user
        response=self.client.post('/login/',data={'email':'mario@testmail.com','password':'i-keep-jumping'})
        self.token=response.data['access_token']
        # create admin user
        self.admin = User(email='admin@mail', password='pass', is_superuser=True, is_staff=True)
        self.admin.save()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    def test_image_add_non_admin(self):
        """
        Ensure image cannot be added by non-admin
        """
        self.api_authentication()
        data={"url":"https://images.daznservices.com/di/library/GOAL/67/ed/thomas-partey-arsenal-2020_1a1h8hhdz7xw611hds7hueajs4.jpg?t=2129690261&quality=100"}
        response=self.client.post('/images/add/',data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_image_add_admin(self):
        """
        Ensure image can be added by admin
        """
        self.client.force_authenticate(user=self.admin)
        data={"url":"https://images.daznservices.com/di/library/GOAL/67/ed/thomas-partey-arsenal-2020_1a1h8hhdz7xw611hds7hueajs4.jpg?t=2129690261&quality=100"}
        response=self.client.post('/images/add/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
