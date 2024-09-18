from django.test import TestCase

from school.models.student import StudentModel


class StudentModelTestCase(TestCase):

    def setUp(self) -> None:
        self.student = StudentModel.objects.create(
            name="John Doe",
            email="email@email.com",
            cpf="08265042051",
            b_day="2000-01-01",
            phone="99 99999-9999",
        )

    def test_student_model_attributes(self):
        """
        Test that checks student attributes.
        """
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.email, "email@email.com")
        self.assertEqual(self.student.cpf, "08265042051")
        self.assertEqual(self.student.b_day, "2000-01-01")
        self.assertEqual(self.student.phone, "99 99999-9999")
