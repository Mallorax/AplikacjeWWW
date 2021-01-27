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
    def test_registration(self):
        data = {"username": "test", "email": "test@test.com",
                "password": "some_passwd"}
        response = self.client.post(reverse("sign-up"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


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


class PersonViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {"first_name": "Jan",
                            "last_name": "Kowal",
                            "tel_number": 583932023}
        self.response = self.client.post(
            reverse("person_create"),
            self.person_data,
            format="json"
        )

    def test_api_can_create_person(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_person_list(self):
        person = Person.objects.get()
        response = self.client.get(
            reverse("person_details", kwargs={'pk': person.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, person)

