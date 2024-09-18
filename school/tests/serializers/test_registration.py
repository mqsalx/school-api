from django.test import TestCase
from rest_framework.utils.serializer_helpers import ReturnDict

from school.models.course import CourseModel
from school.models.registration import RegistrationModel
from school.models.student import StudentModel
from school.serializers.registration import RegistrationSerializer


class RegistrationSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.course_model = CourseModel(
            code="Python",
            description="Python course",
            level="B",
        )

        self.student_model = StudentModel(
            name="John Doe",
            email="email@email.com",
            cpf="08265042051",
            b_day="2000-01-01",
            phone="99 99999-9999",
        )

        self.registration_model = RegistrationModel(
            course=self.course_model,
            student=self.student_model,
            period="N",
        )

        self.registration_serializer = RegistrationSerializer(
            instance=self.registration_model
        )

    @property
    def data(self):
        data = self.registration_serializer.data
        assert isinstance(data, ReturnDict)
        return data

    def test_registration_serializer_keys(self):
        expected_keys = {"id", "course", "student", "period"}
        self.assertEqual(set(self.data.keys()), set(expected_keys))

    def test_registration_serializer_values(self):
        expected_values = {
            "course": self.course_model.id,  # type: ignore
            "student": self.student_model.id,  # type: ignore
            "period": self.registration_model.period,
        }

        for key, value in expected_values.items():
            self.assertEqual(self.data[key], value)
