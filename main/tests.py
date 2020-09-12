from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Person


# Проверка метода POST на создание и наличия обьекта в БД и проверка header и его id
class CreatePersonTest(APITestCase):
    def test_create_person(self):
        url = reverse('person')
        data = {"name": "Ivan", "age": 21, "address": "Lininski", "work": "Prog"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            ('Location', 'https://rsoi-person-service.herokuapp.com/person/{}'.format(Person.objects.get().id)),
            response.headers['Location']
        )
        self.assertEqual(Person.objects.get().name, 'Ivan')
        self.assertEqual(Person.objects.get().age, 21)
        self.assertEqual(Person.objects.get().address, 'Lininski')
        self.assertEqual(Person.objects.get().work, 'Prog')
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('Success, test for creation and availability in the database is completed')


# Проверка работы метода GET persons (что метод GET вытаскивает все значения).
class ExistPersonTest(APITestCase):
    def setUp(self):
        Person.objects.create(name='Mary', age=23, address='Iasnaia 5', work='Poduser')
        Person.objects.create(name='Egor', age=21, address='Lininski', work='Prog')

    def test_exist_person(self):
        response = self.client.get(reverse('persons'))
        self.assertTrue(
            {'id': 1, 'name': 'Mary', 'age': '23', 'address': 'Iasnaia 5', 'work': 'Poduser'},
            {'id': 2, 'name': 'Egor', 'age': '21', 'address': 'Lininski', 'work': 'Prog'}
            in response.json().get('persons')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Success, test to exists in the database is completed')

    # def test
