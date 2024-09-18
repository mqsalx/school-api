from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models.course import CourseModel
from school.models.registration import RegistrationModel
from school.models.student import StudentModel
from school.serializers.registration import RegistrationSerializer


class RegistrationUrlTestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", password="admin", email="admin@example.com"
        )
        self.client.force_authenticate(user=self.superuser)  # type: ignore
        self.url = reverse("registrations-list")
        self.course_one = CourseModel.objects.create(
            code="Python",
            description="Python course",
            level="A",
        )

        self.course_two = CourseModel.objects.create(
            code="JavaScript",
            description="JavaScript course",
            level="B",
        )
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
        self.registration_one = RegistrationModel.objects.create(
            course=self.course_one,
            student=self.student_one,
            period="N",
        )
        self.registration_two = RegistrationModel.objects.create(
            course=self.course_two,
            student=self.student_two,
            period="M",
        )

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
