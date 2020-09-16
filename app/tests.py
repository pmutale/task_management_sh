from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Task


class TaskTest(APITestCase):
    def test_task__create(self):
        """
        Test if we can create a new task object.
        """
        url = reverse('task')
        data = {'name': 'A task from test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'A task from test')

