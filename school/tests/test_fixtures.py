from django.test import TestCase

from school.models.course import CourseModel
from school.models.student import StudentModel


class FixturesTestCase(TestCase):
    fixtures = ["utils/school_prototype_db.json"]

    def test_schools(self):
        """
        Testing schools fixtures.
        """

        students = StudentModel.objects.get(cpf="13148555651")
        courses = CourseModel.objects.get(pk=4)

        self.assertEqual(students.phone, "21 98796-7451")
        self.assertEqual(courses.code, "CPOO3")
