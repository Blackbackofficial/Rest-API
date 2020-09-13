from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Person


# Тесты по API Person:
# 1) Метода POST (/person), создание и наличие обьекта в БД, проверка header и его {id}
# 2) Метода GET (/persons), все значения
# 3) Метода DELETE (/person/{id}), + проверка на отсутствие
# 4) Метода GET (/person/{id})
# 5) Метод PATCH (/person/{id})

class API_Person_Test(APITestCase):
    def setUp(self):
        Person.objects.create(name='Mary', age=23, address='Iasnaia 5', work='Poduser')
        Person.objects.create(name='Egor', age=21, address='Lininski', work='Prog')

    # def test_create_person(self):
    #     url = reverse('creat_persons')
    #     data = {'name': 'Ivan', 'age': 21, 'address': 'Lininski', 'work': 'Prog'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(
    #         ('Location', 'https://rsoi-person-service.herokuapp.com/person/{}'.format(Person.objects.get(id=3).id)),
    #         response.headers['Location']
    #     )
    #     self.assertEqual(Person.objects.get(id=3).name, 'Ivan')
    #     self.assertEqual(Person.objects.get(id=3).age, 21)
    #     self.assertEqual(Person.objects.get(id=3).address, 'Lininski')
    #     self.assertEqual(Person.objects.get(id=3).work, 'Prog')
    #     self.assertEqual(Person.objects.count(), 3)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     print('Success, test method POST for creation and availability in the database is completed')

    def test_exist_person(self):
        response = self.client.get(reverse('all_persons'))
        self.assertTrue(
            {'id': 1, 'name': 'Mary', 'age': '23', 'address': 'Iasnaia 5', 'work': 'Poduser'},
            {'id': 2, 'name': 'Egor', 'age': '21', 'address': 'Lininski', 'work': 'Prog'}
            in response.json().get('persons')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Success, test method GET to exists in the database is completed')

    def test_delete_person(self):
        url = reverse('up_del_person', args='1')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 1)
        url = reverse('get_persons', args='1')
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
        print('Success, test for DELETE person is completed')

    def test_get_person_for_id(self):
        url = reverse('get_persons', args='2')
        response = self.client.get(url)
        self.assertEqual(
            {'id': 2, 'name': 'Egor', 'age': 21, 'address': 'Lininski', 'work': 'Prog'},
            response.json()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Success, test for GET person for ID is completed')

    def test_update_person_for_id(self):
        url = reverse('up_del_person', args='1')
        data = {'age': 22, 'address': 'Sokolniki'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        person_DB = Person.objects.get(id=1)
        self.assertEqual(person_DB.age, 22)
        self.assertEqual(person_DB.address, 'Sokolniki')
        self.assertEqual(person_DB.name, 'Mary')
        self.assertEqual(person_DB.work, 'Poduser')
        print('Success, test PATCH for person is completed')
