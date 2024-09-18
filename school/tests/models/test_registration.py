from django.test import TestCase

from school.models.course import CourseModel
from school.models.registration import RegistrationModel
from school.models.student import StudentModel


class RegistrationModelTestCase(TestCase):

    def setUp(self) -> None:
        self.course = CourseModel.objects.create(
            code="Python",
            description="Python course",
            level="B",
        )

        self.student = StudentModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            cpf="12345678901",
            b_day="2000-01-01",
            phone="1234567890",
        )

        self.registration = RegistrationModel.objects.create(
            course=self.course,
            student=self.student,
            period="N",
        )

    def test_registration_model_attributes(self):
        """
        Test that checks registration attributes.
        """
        self.assertEqual(self.registration.course, self.course)
        self.assertEqual(self.registration.student, self.student)
        self.assertEqual(self.registration.period, "N")
