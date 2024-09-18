from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models.student import StudentModel
from school.serializers.student import StudentSerializer


class StudentUrlTestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", password="admin", email="admin@example.com"
        )
        self.client.force_authenticate(user=self.superuser)  # type: ignore
        self.url = reverse("students-list")
        self.student_one = StudentModel.objects.create(
            name="John Doe",
            email="emailstudentone@email.com",
            cpf="08265042051",
            b_day="2000-01-01",
            phone="99 99999-9999",
        )
        self.student_two = StudentModel.objects.create(
            name="Mary Jane",
            email="emailstudenttwo@email.com",
            cpf="1937153162",
            b_day="1999-01-01",
            phone="99 99999-9999",
        )

    def test_student_url_list(self):
        """
        Testing GET request to list students.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_url_retrieve(self):
        """
        Testing GET request to list specific student.
        """
        response = self.client.get(self.url + f"{self.student_one.id}/")  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_student = StudentModel.objects.get(pk=self.student_one.id)  # type: ignore
        data_student_serialized = StudentSerializer(instance=data_student).data
        self.assertEqual(response.data, data_student_serialized)  # type: ignore

    def test_student_url_create(self):
        """
        Testing POST request to create a student.
        """
        data = {
            "name": "John Doe",
            "email": "emailjd@email.com",
            "cpf": "54058340096",
            "b_day": "2000-01-01",
            "phone": "48 99999-9999",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_url_destroy(self):
        """
        Testing DELETE request to delete a student.
        """
        response = self.client.delete(f"{self.url}{self.student_two.id}/")  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_student_url_update(self):
        """
        Testing PUT request to update a student.
        """
        data = {
            "name": "John Doe",
            "email": "emailjd@email.com",
            "cpf": "36816883039",
            "b_day": "2000-01-01",
            "phone": "48 99999-9999",
        }
        response = self.client.put(f"{self.url}{self.student_two.id}/", data=data)  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_200_OK)
