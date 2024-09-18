from django.test import TestCase

from school.models.course import CourseModel


class CourseModelTestCase(TestCase):

    def setUp(self) -> None:
        self.course = CourseModel.objects.create(
            code="Python",
            description="Python course",
            level="B",
        )

    def test_course_model_attributes(self):
        """
        Test that checks course attributes.
        """
        self.assertEqual(self.course.code, "Python")
        self.assertEqual(self.course.description, "Python course")
        self.assertEqual(self.course.level, "B")
