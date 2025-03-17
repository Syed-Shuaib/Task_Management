from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(title="Test Task", description="Test Description", status="pending")
        self.valid_data = {"title": "Updated Task", "description": "Updated Description", "status": "completed"}
    
    def test_list_tasks(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task(self):
        response = self.client.get("/api/v1/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {"title": "New Task", "description": "New Description", "status": "pending"}
        response = self.client.post("/api/v1/tasks/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        response = self.client.put("/api/v1/tasks/1/", self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete("/api/v1/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
