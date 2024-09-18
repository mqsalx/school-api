from django.test import TestCase
from rest_framework.utils.serializer_helpers import ReturnDict

from school.models.student import StudentModel
from school.serializers.student import StudentSerializer


class StudentSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.student_model = StudentModel(
            name="John Doe",
            email="email@email.com",
            cpf="08265042051",
            b_day="2000-01-01",
            phone="99 99999-9999",
        )

        self.student_serializer = StudentSerializer(
            instance=self.student_model
        )

    @property
    def data(self):
        data = self.student_serializer.data
        assert isinstance(data, ReturnDict)
        return data

    def test_student_serializer_keys(self):
        expected_keys = {"id", "name", "email", "cpf", "b_day", "phone"}
        self.assertEqual(set(self.data.keys()), set(expected_keys))

    def test_student_serializer_values(self):
        expected_values = {
            "name": self.student_model.name,
            "email": self.student_model.email,
            "cpf": self.student_model.cpf,
            "b_day": self.student_model.b_day,
            "phone": self.student_model.phone,
        }

        for key, value in expected_values.items():
            self.assertEqual(self.data[key], value)
