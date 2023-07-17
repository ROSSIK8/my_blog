from unittest import TestCase
from rest_framework.test import APIClient


class TestsMyBlog(TestCase):
    def test_successful_request(self):
        url = '/articles/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
