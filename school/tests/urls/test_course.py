from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models.course import CourseModel
from school.serializers.course import CourseSerializer


class CourseUrlTestCase(APITestCase):
    fixtures = ["utils/school_prototype_db.json"]

    def setUp(self):
        self.user = User.objects.get(username="administrator")
        self.client.force_authenticate(user=self.user)  # type: ignore
        self.url = reverse("students-list")
        self.course_one = CourseModel.objects.get(pk=1)
        self.course_two = CourseModel.objects.get(pk=2)
        self.url = reverse("courses-list")

    def test_course_url_list(self):
        """
        Testing GET request to list courses.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_url_retrieve(self):
        """
        Testing get request to list specific course.
        """
        response = self.client.get(self.url + f"{self.course_two.id}/")  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data_course = CourseModel.objects.get(pk=self.course_two.id)  # type: ignore
        data_course_serialized = CourseSerializer(instance=data_course).data
        self.assertEqual(response.data, data_course_serialized)  # type: ignore

    def test_course_url_create(self):
        """
        Testing POST request to create a course.
        """
        data = {"code": "Csharp", "description": "Python course", "level": "A"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_url_destroy(self):
        """
        Testing DELETE request to delete a course.
        """
        response = self.client.delete(f"{self.url}{self.course_two.id}/")  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_course_url_update(self):
        """
        Testing PUT request to update a course.
        """
        data = {
            "code": "JavaScript",
            "description": "JavaScript",
            "level": "I",
        }
        response = self.client.put(f"{self.url}{self.course_two.id}/", data=data)  # type: ignore
        self.assertEqual(response.status_code, status.HTTP_200_OK)
