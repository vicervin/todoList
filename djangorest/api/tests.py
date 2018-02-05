from django.test import TestCase
from .models import ToDoList
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse



class ModelTestCase(TestCase):
    """ This is a test suite for the todoList model """

    def setUp(self):
        self.ToDoList_name = "ShoppingList"
        self.ToDoList = ToDoList(name=self.ToDoList_name)

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
        self.client = APIClient()
        self.todolist_data = { 'name': "ShoppingList"}
        self.response = self.client.post(
            reverse('create'),
            self.todolist_data,
            format="json"
        )

    def test_CreateTodolist_via_api(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_readTodolist_via_api(self):
        """ Checks if the API gets the todolist """
        todolist = ToDoList.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todolist)

    def test_updateTodolist_via_api(self):
        todolist = ToDoList.objects.get()
        update_todolist = {'name': 'ShoppingListHome'}
        response = self.client.put(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            update_todolist,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleteTodolist_via_api(self):
        todolist = ToDoList.objects.get()
        response = self.client.delete(
            reverse('details',
                    kwargs={'pk': todolist.id}),
            format='json',
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
