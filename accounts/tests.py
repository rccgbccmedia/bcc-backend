from django.test import TestCase
from .models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse



# Create your tests here.


class Accounts(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(
            email='felix@testmail.com', first_name='felix', last_name='bull', phone='+2342933409812', address= "here")
        User.objects.create(
            email='sophia@testmail.com', first_name='sophia', last_name='fencer', phone="+2342933409812", address= "here")

    def test_User_organisation(self):
        user_felix = User.objects.get(email='felix@testmail.com')
        user_sophia = User.objects.get(email='sophia@testmail.com')
        self.assertEqual(
            user_felix.last_name, "bull")
        self.assertEqual(
            user_sophia.first_name, "sophia")


class RegistrationTestCase(APITestCase):
    """ Test module for user registration """

    def test_registration(self):
        data={"first_name":"lynn","last_name":"frank","password":"PASwwordLit","email":"lynn@gmail.com","phone":"+23408122633167","address":"here"}
        response=self.client.post('/register/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


  

class UserDetailsTestCase(APITestCase):
    def setUp(self):
        # create a new user by making a post request to register endpoint
        self.user=self.client.post('/register/',data={'email':'mario@testmail.com','password':'i-keep-jumping', 'first_name':'mario', 'last_name':'icardi', 'phone': '+2348122633167', 'address': "here"})
        # obtain a json web token for the newly created user
        response=self.client.post('/login/',data={'email':'mario@testmail.com','password':'i-keep-jumping'})
        self.token=response.data['access_token']
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    # check to retrieve details of the authenticated user
    def test_user_detail_retrieve(self):
        # print(User.objects.filter(pk=2))
        response=self.client.get(reverse('user-details'))
        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    # check to retrieve details of unauthenticated user
    def test_user_details_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(reverse('user-details'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)