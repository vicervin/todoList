from django.test import TestCase
from .models import ToDoList
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    """ This is a test suite for the todoList model """

    def setUp(self):
        """ Define test client and test variables"""
        user = User.objects.create(username="codine")
        self.ToDoList_name = "ShoppingList"
        self.ToDoList = ToDoList(name=self.ToDoList_name, owner=user)

    def test_model_creates_todolist(self):
        old_count = ToDoList.objects.count()
        self.ToDoList.save()
        new_count = ToDoList.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_todolist_default_status(self):
        self.assertEqual(False, self.ToDoList.done)


class ViewTestCase(TestCase):
    """ todoList View Test Suite """

    def setUp(self):
        """ Define client and test variables"""

        user = User.objects.create(username="codine")
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.todolist_data = {'name': "Travelling Checklist", 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.todolist_data,
            format="json"
        )

    def test_create_todolist_via_api(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_read(self):
        new_client = APIClient()
        response = new_client.get(
                        '/todolists/',
                        kwargs={'pk': 3},
                        format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_todolist_via_api(self):
        """ Checks if the API gets the todolist """
        todolist = ToDoList.objects.get(id=1)
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todolist)

    def test_update_todolist_via_api(self):
        todolist = ToDoList.objects.get()
        update_todolist = {'name': 'ShoppingListHome'}
        response = self.client.put(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            update_todolist,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todolist_via_api(self):
        todolist = ToDoList.objects.get()
        response = self.client.delete(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            format='json',
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
