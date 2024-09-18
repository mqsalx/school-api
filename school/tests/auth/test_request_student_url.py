from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RequestGetStudentTestCase(APITestCase):
    """
    Test case for the 'students-list' API endpoint.
    This test case includes tests for both authorized and unauthorized GET requests.
    """

    def setUp(self):
        """
        Set up the test case environment.
        Creates a user and sets the URL for the 'students-list' endpoint.
        """
        self.user = User.objects.create_user(
            username="admin",
            password="admin",
        )
        self.url = reverse("students-list")

    def test_request_get_authorized(self):
        """
        Test that verifies the authenticity of a user with valid credentials
        """
        self.client.force_authenticate(self.user)  # type: ignore
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_not_authorized(self):
        """
        Test that verifies the authenticity of a user with invalid credentials
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
