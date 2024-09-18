from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models.course import CourseModel
from school.models.registration import RegistrationModel
from school.models.student import StudentModel
from school.serializers.registration import RegistrationSerializer


class RegistrationUrlTestCase(APITestCase):
    fixtures = ["utils/school_prototype_db.json"]

    def setUp(self):
        self.user = User.objects.get(username="administrator")
        self.client.force_authenticate(user=self.user)  # type: ignore
        self.url = reverse("registrations-list")
        self.student_one = StudentModel.objects.get(pk=1)
        self.student_two = StudentModel.objects.get(pk=2)
        self.course_one = CourseModel.objects.get(pk=1)
        self.course_two = CourseModel.objects.get(pk=2)
        self.registration_one = RegistrationModel.objects.get(pk=1)
        self.registration_two = RegistrationModel.objects.get(pk=2)

    def test_registration_url_list(self):
        """
        Testing GET request to list registrations.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registration_url_retrieve(self):
        """
        Testing get request to list specific registration.
        """
        response = self.client.get(self.url + f"{self.registration_one.id}/")  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_registration = RegistrationModel.objects.get(pk=self.registration_one.id)  # type: ignore
        data_registration_serialized = RegistrationSerializer(
            instance=data_registration
        ).data
        self.assertEqual(response.data, data_registration_serialized)  # type: ignore

    def test_registration_url_create(self):
        """
        Testing POST request to create a registration.
        """
        data = {
            "course": self.course_one.id,  # type: ignore
            "student": self.student_one.id,  # type: ignore
            "period": "N",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_url_destroy(self):
        """
        Testing DELETE request to delete a registration.
        """
        response = self.client.delete(f"{self.url}{self.registration_two.id}/")  # type: ignore
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_registration_url_update(self):
        """
        Testing PUT request to update a registration.
        """
        data = {
            "course": self.course_one.id,  # type: ignore
            "student": self.student_one.id,  # type: ignore
            "period": "M",
        }
        response = self.client.put(f"{self.url}{self.registration_two.id}/", data=data)  # type: ignore
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
