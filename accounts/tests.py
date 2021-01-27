from django.contrib.auth import authenticate
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from tasks.models import Person, Task
from rest_framework.test import APIClient
from tasks.serializers import TaskSerializer, PersonSerializer
import json


class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class PersonTestCase(APITestCase):

    def setUp(self):
        self.first_name = "Jan"
        self.last_name = "Kowal"
        self.tel_number = 342845432
        self.person = Person(first_name=self.first_name,
                             last_name=self.last_name,
                             tel_number=self.tel_number)

    def test_model_can_create_a_person(self):
        old_count = Person.objects.count()
        self.person.save()
        new_count = Person.objects.count()
        self.assertNotEqual(old_count, new_count)


class PersonListViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('person_list'), follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


