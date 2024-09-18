from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin", password="admin"
        )

    def test_authenticate_user_valid_credentials(self):
        """
        Test that verifies the authenticity of a user with valid credentials
        """
        user = authenticate(username="admin", password="admin")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_authenticate_user_invalid_username(self):
        """
        Test that verifies the authenticity of a user with invalid username
        """
        user = authenticate(username="admin@", password="admin")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authenticate_user_invalid_password(self):
        """
        Test that verifies the authenticity of a user with invalid password
        """
        user = authenticate(username="admin", password="admin@")
        self.assertFalse((user is not None) and user.is_authenticated)
