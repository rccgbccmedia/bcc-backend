from django.test import TestCase
from .models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse



# Create your tests here.


class EventsGetCreateUpdateTestCase(APITestCase):

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

    def test_event_creation_non_admin(self):
        """
        Ensure event cannot be created by non-admin
        """
        self.api_authentication()
        data={"name":"sunday service","venue":"church premsesis","time":"2015-01-12T01:32","description":"holds every sunday","capacity":"100"}
        response=self.client.post('/events/create/',data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    
    def test_event_creation_admin(self):
        """
        Ensure event can be created by admin
        """
        self.client.force_authenticate(user=self.admin)
        data={"name":"sunday service","venue":"church premsesis","time":"2015-01-12T01:32","description":"holds every sunday","capacity":"100"}
        response=self.client.post('/events/create/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_event_update(self):
        """
        Ensure an event is able to update
        """
        self.client.force_authenticate(user=self.admin)
        data={"name":"sunday service","venue":"church premsesis","time":"2015-01-12T01:32","description":"holds every sunday","capacity":"100"}
        response=self.client.post('/events/create/',data)
        updated_data={"name":"sunday service","venue":"new site","time":"2015-01-12T01:32","description":"holds every sunday","capacity":"100"}
        url = "/events/update/"
        event_id = response.data['id']
        final_url = f'{url}{event_id}/'
        updated_response = self.client.put(final_url, updated_data)
        self.assertEqual(updated_response.data['venue'],'new site')


class RsvpCreateTestCase(APITestCase):

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


    def test_create_and_get_rsvp(self):
        """
        Ensure user can get and create rsvp
        """

        # create an event to test with
        self.client.force_authenticate(user=self.admin)
        data={"name":"sunday service","venue":"church premsesis","time":"2015-01-12T01:32","description":"holds every sunday","capacity":"100"}
        response=self.client.post('/events/create/',data)
        event_id = response.data['id']

        # try to create rsvp for unauthenticated user 
        self.client.force_authenticate(user=None, token=None)
        # data = {"event":event_id, "seat": 23}
        url = f'/events/{event_id}/rsvp/'
        response = self.client.post(url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

        # try to create rsvp for authenticated user
        self.api_authentication()
        url = f'/events/{event_id}/rsvp/'
        response = self.client.post(url)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        # try to get all rsvps of authenticated user
        url = "/rsvp/"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)





