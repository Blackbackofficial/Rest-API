from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Person


# Проверка метода POST на создание и наличия обьекта в БД и проверка header и его id
class CreatePersonTest(APITestCase):
    def test_create_person(self):
        url = reverse('person')
        data = {"person": "Ivasik"}
        response = self.client.post(url, data, format='json')
        print(response.headers['Location'])
        self.assertEqual(
            ('Location', 'https://rsoi-person-service.herokuapp.com/person/{}'.format(Person.objects.get().id)),
            response.headers['Location']
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().person, 'Ivasik')
        print('Success, test for creation and availability in the database is completed')


# Проверка работы метода GET persons (что метод GET вытаскивает все значения).
class ExistPersonTest(APITestCase):
    def setUp(self):
        Person.objects.create(person='Mary')
        Person.objects.create(person='Egor')

    def test_exist_person(self):
        response = self.client.get(reverse('persons'))
        self.assertTrue({'person': 'Mary'}, {'person': 'Egor'} in response.json().get('persons'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Success, test to exists in the database is completed')

    # def test
