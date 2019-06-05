import datetime

from django.test import TestCase
from django.urls import reverse_lazy, reverse
from rest_framework import status

from todo import views, models

TodoListURL = reverse(views.TodoListView.name)


class TodoListTest(TestCase):

    def test_get_todo(self):
        """Test of method get"""
        res = self.client.get(TodoListURL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        """Test of creating new object and returning properly data after create"""
        payload = {"title": "Conquer the world", "done": True}
        res = self.client.post(TodoListURL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {'task_id': 1})

    def test_not_create_todo(self):
        """Test if done: False, and done_data: not null will return status 400"""
        payload = {"title": "Conquer the world", "done": False, "done_date": "2019-05-10, 19:59:28"}
        res = self.client.post(TodoListURL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_data_create(self):
        """Test if data_create is automatic add """
        todo_object = models.TodoList.objects.create(title = "ss", done = True)
        self.assertEqual(todo_object.done_date, datetime.datetime.utcnow().strftime("%Y-%m-%d, %H:%M:%S"))

    def test_get_detail_list(self):
	"""Test get method of detatil todo """
        self.todo = models.TodoList.objects.create(title = "ss", done = True)
        url = reverse_lazy(views.TodoDetailView.name, kwargs = {'pk': self.todo.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_patch_detail_list(self):
	"""Test of patch method """
        self.todo = models.TodoList.objects.create(title = "ss", done = True)
        url = reverse_lazy(views.TodoDetailView.name, kwargs = {'pk': self.todo.pk})
        res = self.client.patch(url, done = False)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_does_not_exist_detail_list(self):
	"""Test if try delete nit exist todo return 404 status """
        url = reverse_lazy(views.TodoDetailView.name, kwargs = {'pk': 1})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


