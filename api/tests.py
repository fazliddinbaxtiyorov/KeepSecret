from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class QuestTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all(self):
        response = self.client.get('/quests/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testing_none_page(self):
        response = self.client.get('/none/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_website(self):
        self.client = APIClient()
        response = self.client.get('hello/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def testing_search(self):
        response = self.client.get('/api/search/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)